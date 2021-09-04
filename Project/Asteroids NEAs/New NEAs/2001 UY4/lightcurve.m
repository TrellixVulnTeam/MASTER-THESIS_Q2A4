clear all;
close all;
clc;

% Import data from cvs file
data=csvread('Light curve.csv', 4);
col1 = data(:, 1);
col2 = data(:, 2);
col3 = data(:, 3);
col4 = data(:, 4);

t = 0:numel(col1);
xy = [col1; col4];
pp = spline(t, xy);
tInterp = linspace(1,numel(col1));
xyInterp = ppval(pp, tInterp);

% Plotting the light curve
figure
scatter(col1, col2, '+', 'linewidth',1.5)
hold on

plot(xyInterp(1,:),xyInterp(2,:))
hold off 

title('2001 UY4 Light Curve', 'FontSize', 16)
xlabel('Phase [Period = 6.7970 Hours]', 'fontweight','bold','fontsize',12)
ylabel('Magnitude', 'fontweight','bold','fontsize',12)
set(gca, 'ydir', 'reverse')
grid on
grid minor
legend('Data of 4 Nights', '6th order', 'fontweight','bold','fontsize',12 )
