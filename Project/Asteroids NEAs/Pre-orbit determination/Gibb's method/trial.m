% Gibbs Method
%
% v2 - the velocity corresponding to r2 (km/s)
% coe - orbital elements [h e RA incl w TA a]
% h = angular momentum (kmˆ2/s)
% e = eccentricity
% RA = right ascension of the ascending
% node (rad)
% incl = orbit inclination (rad)
% w = argument of perigee (rad)
% TA = true anomaly (rad)
% a = semimajor axis (km)
% T - period of elliptic orbit (s)
% ------------------------------------------------------------
clear; 
clc;
deg = pi/180;     % radians to degree conversion
global mu
au = 149597870.7; % Km
mu = 398600.4418; % gravitational parameter

% IVAR 1627
% r1 = [-2.119388265311549, 0.9135726614117664, 0.1362922667619230];
% r2 = [-2.120052486075107, 0.9031999459944826, 0.1374185903074423];
% r3 = [-2.120546166419217, 0.8948227605051885, 0.1383235972986717];
% r1 = [1.094313940666847 1.453361244265937 -2.665681549832875e-01];
% r2 = [1.088021004406742 1.464428569258595 -2.670108183228992e-01];
% r3 = [1.081676432465787 1.475427096848251 -2.674408931462609e-01];

% 1998 TU3
% r1 = [1.159264044681950,  1.200490865865283e-01, -1.095671113508057e-01];
% r2 = [1.157171419681076,  1.413060802814081e-01, -1.097991800960494e-01];
% r3 = [1.156858200596059,  1.439494165870326e-01, -1.098231294736614e-01];
% r1 = [-6.221566736326280e-02 -5.380324905304337e-01 1.585890562337718e-02];
% r2 = [-3.895362051574176e-02 -5.504402979288572e-01 1.394844688175687e-02];
% r3 = [-1.563784063245847e-02 -5.618926368971378e-01 1.201419365429728e-02];

% 2000 QL7
r1 = [-1.122518886726144 -3.261169859270553 -1.108747744758537];
r2 = [-1.116806655155184 -3.264087400211805 -1.108943180201054];
r3 = [-1.111087527005574 -3.266984642050584 -1.109131725920097];

% 2001 sg276
% r1 = [-1.156528433091796 1.149847675000554e-01 3.774618314954212e-01];
% r2 = [-1.156521834138001 9.945634486439929e-02 3.710795460654758e-01];
% r3 = [-1.156323708101620 8.391208853997528e-02 3.646354085833321e-01];

% 2001 UY4
% r1 = [4.037568883207751e-01 2.464531728576342 -2.338621097899097e-01];
% r2 = [3.991380432102868e-01 2.467859914407152 -2.340169028754116e-01];
% r3 = [3.945115632022339e-01 2.471141871813709 -2.341673018870743e-01];

% 2003 rp8 good
r1 = [-1.366252302860174 -6.961593362438063e-01 -9.244568567449476e-01];
r2 = [-1.357097526395703 -7.047040111111852e-01 -9.224152092649917e-01];
r3 = [-1.347872182678872 -7.132115825478252e-01 -9.203253219400799e-01];

% Input data
fprintf('---------------------------------------------------')
fprintf('\n Gibbs Method\n')
fprintf('\n\n Input data:\n')
fprintf('\n Gravitational parameter (kmˆ3/sˆ2) = %g\n', mu)
fprintf('\n r1 (au) = [%g %g %g]', r1(1), r1(2), r1(3))
fprintf('\n r2 (au) = [%g %g %g]', r2(1), r2(2), r2(3))
fprintf('\n r3 (au) = [%g %g %g]', r3(1), r3(2), r3(3))
fprintf('\n\n');
%...Algorithm 5.1:
[v2, ierr] = gibbs(r1, r2, r3);

%If the vectors r1, r2, r3, are not coplanar, abort:
if ierr == 1
    fprintf('\n These vectors are not coplanar.\n\n')
return
end

coe = coe_from_sv(r2,v2);
h = coe(1);
e = coe(2);
RA = coe(3);
incl = coe(4);
w = coe(5);
TA = coe(6);
a = coe(7);

%Preliminary orbital elements
fprintf(' Solution:')
fprintf('\n');
fprintf('\n v2 (km/s) = [%g %g %g]', v2(1), v2(2), v2(3))
fprintf('\n\n Orbital elements:');
fprintf('\n Angular momentum (kmˆ2/s)   = %g', h)
fprintf('\n Eccentricity                = %g', e)
fprintf('\n Inclination (deg)           = %g', incl/deg)
fprintf('\n RA of ascending node (deg)  = %g', RA/deg)
fprintf('\n Argument of perigee (deg)   = %g', w/deg)
fprintf('\n True anomaly (deg)          = %g', TA/deg)
fprintf('\n Semimajor axis (AU)         = %g', a)

% If the orbit is an ellipse, output the period:
if e < 1
    T = (2*pi/sqrt(mu)*a^1.5)*100;
    %T_ast = T/(24*3600*60*365);
    fprintf('\n Period (years)              = %g', T)
end
fprintf('\n-----------------------------------------------\n')
