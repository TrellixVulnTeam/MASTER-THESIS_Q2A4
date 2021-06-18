clear all;
close all;
clc;

% Import data from cvs file
data=csvread('Light curve.csv', 4);
col1 = data(:, 1);
col2 = data(:, 2);
col3 = data(:, 3);
col4 = data(:, 4);

% Plotting the light curve
figure
scatter(col1, col2, '+', 'linewidth',1.5)
hold on

scatter(col1, col4, 'filled')
hold off 

title('1998 TU3 Light Curve', 'FontSize', 16)
xlabel('Phase [Period = 2.3777 Hours]', 'fontweight','bold','fontsize',12)
ylabel('Magnitude', 'fontweight','bold','fontsize',12)
set(gca, 'ydir', 'reverse')
grid on
grid minor
legend('Data of 5 Nights', '4th order', 'fontweight','bold','fontsize',12 )
