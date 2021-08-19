%  Lambert’s problem Method
%
% deg - factor for converting between degrees and radians
% pi - 3.1415926...
% mu - gravitational parameter (kmˆ3/sˆ2)
% r1, r2 - initial and final position vectors (km)
% dt - time between r1 and r2 (s)
% string - = 'pro' if the orbit is prograde
% = 'retro' if the orbit is retrograde
% v1, v2 - initial and final velocity vectors (km/s)
% coe - orbital elements [h e RA incl w TA a]
% where h = angular momentum (kmˆ2/s)
% e = eccentricity
% RA = right ascension of the ascending node
% (rad)
% incl = orbit inclination (rad)
% w = argument of perigee (rad)
% TA = true anomaly (rad)
% a = semimajor axis (km)
% TA1 - Initial true anomaly
% TA2 - Final true anomaly
% T - period of an elliptic orbit

% -----------------------------------------------------------
clear var;
close all;
clc;

global mu
au = 149597870.7;
deg = pi/180;
mu_e = 398600.4418;
mu = 1.3271244e11; % Sun's Gravitational Parameter

% IVAR aug 10, 11
% r1 = [-2.119388265311549 0.9135726614117664 0.1362922667619230]*au;
% r2 = [-2.120052486075107 0.9031999459944826 0.1374185903074423]*au;
% dt = 91500; % 25 hours and 25 minutes
% r1 = [1.094313940666847 1.453361244265937 -2.665681549832875e-01]*au;
% r2 = [1.088021004406742 1.464428569258595 -2.670108183228992e-01]*au;
% dt = 86400;

% 1998 TU3
% r1 = [1.159264044681950 1.200490865865283e-01 -1.095671113508057e-01]*au;
% r2 = [1.157171419681076 1.413060802814081e-01 -1.097991800960494e-01]*au;
% dt = 161280; % 44 hours and 48 minutes
% r1 = [-6.221566736326280e-02 -5.380324905304337e-01 1.585890562337718e-02]*au;
% r2 = [-3.895362051574176e-02 -5.504402979288572e-01 1.394844688175687e-02]*au;
% dt = 86400.0;

% 2000 QL7
% r1 = [-1.042940617684813e-01 3.471900026823399e-01 2.140864560411465e-01]*au;
% r2 = [-1.080504664300751e-01 3.528128145199558e-01 2.108458444358209e-01]*au;
% r1 = [-1.122518886726144 -3.261169859270553 -1.108747744758537]*au;
% r2 = [-1.116806655155184 -3.264087400211805 -1.108943180201054]*au;
% dt = 86400;
% dt = 73861; % 20 hours and 51 minutes

% 2001 sg276
% r1 = [-1.156528433091796 1.149847675000554e-01 3.774618314954212e-01]*au;
% r2 = [-1.156521834138001 9.945634486439929e-02 3.710795460654758e-01]*au;
% dt = 86400;

% 2003 RP8
% r1 = [-1.366252302860174 -6.961593362438063e-01 -9.244568567449476e-01]*au;
% r2 = [-1.271521636069843 -7.798457179155895e-01 -9.018371029986981e-01]*au;
r1 = [-1.366252302860174 -6.961593362438063e-01 -9.244568567449476e-01]*au;
r2 = [-1.357097526395703 -7.047040111111852e-01 -9.224152092649917e-01]*au;
dt = 86400;

% 2001 UY4
% r1 = [4.037568883207751e-01 2.464531728576342 -2.338621097899097e-01]*au;
% r2 = [3.991380432102868e-01 2.467859914407152 -2.340169028754116e-01]*au;
% dt = 86400; % 24 hours

string = 'pro'; % orbit type

%...
[v1, v2] = lambert(r1, r2, dt, string);
% using r1 and v1:
coe = coe_from_sv(r1, v1);
%...Save the initial true anomaly:
TA1 = coe(6);
%...Algorithm 4.1 (using r2 and v2):
coe = coe_from_sv(r2, v2);
%...Save the final true anomaly:
TA2 = coe(6)/deg;
ec = coe(2);
% mean anomaly
% MA = TA2 + (2*sin(TA2)) + (0.75*ec^2 + 0.125*ec^4)*sin(3*TA2) - (1/3 * ec^3)*sin(3*TA2) + (5/32 * ec^4)*sin(4*TA2);
%...Echo the input data and output the results to the command window:
fprintf('---------------------------------------------------')
fprintf('\n Lambert''s Problem\n')
fprintf('\n\n Input data:\n');
fprintf('\n Gravitational parameter (kmˆ3/sˆ2) = %g\n', mu)
fprintf('\n r1 (km) = [%g %g %g]', ...
r1(1), r1(2), r1(3))
fprintf('\n r2 (km) = [%g %g %g]', ...
r2(1), r2(2), r2(3))
fprintf('\n Elapsed time (s) = %g', dt);
fprintf('\n\n Solution:\n')
fprintf('\n v1 (km/s) = [%g %g %g]', ...
v1(1), v1(2), v1(3))
fprintf('\n v2 (km/s) = [%g %g %g]', ...
v2(1), v2(2), v2(3))
fprintf('\n\n Orbital elements:')
fprintf('\n Angular momentum (kmˆ2/s)   = %g', coe(1))
fprintf('\n Eccentricity                = %g', coe(2))
fprintf('\n Inclination (deg)           = %g', coe(4)/deg)
fprintf('\n RA of ascending node (deg)  = %g', coe(3)/deg)
fprintf('\n Argument of perigee (deg)   = %g', coe(5)/deg)
fprintf('\n True anomaly initial (deg)  = %g', TA1/deg)
fprintf('\n True anomaly final (deg)    = %g', TA2)
% fprintf('\n Mean Anomaly (deg) = %g', MA)
fprintf('\n Semimajor axis (AU)         = %g', coe(7)/au)
fprintf('\n Periapse radius (AU)        = %g', ...
(coe(1)^2/mu/(1 + coe(2)))/au)
if coe(2)<1
    T = 2*pi/sqrt(mu)*coe(7)^1.5;
    Tast = (2*pi/sqrt(mu_e)*(coe(7)/au)^1.5)*100;
    fprintf('\n\n Period:')
    fprintf('\n Seconds                     = %g', T)
    fprintf('\n Minutes                     = %g', T/60)
    fprintf('\n Hours                       = %g', T/3600)
    fprintf('\n Days                        = %g', T/24/3600)
    fprintf('\n Years                       = %g', Tast)
end
fprintf('\n-----------------------------------------------\n')