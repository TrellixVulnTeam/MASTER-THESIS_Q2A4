clear all;
close all;
clc;

% Import data from cvs file
data=csvread('new light curve.csv', 4);
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

title('2000 QL7 Light Curve', 'FontSize', 16)
xlabel('Phase [Period = 2.3750 Hours]', 'fontweight','bold','fontsize',12)
ylabel('Magnitude', 'fontweight','bold','fontsize',12)
set(gca,'XLim',[0 1])
set(gca, 'ydir', 'reverse')
grid on
grid minor
legend('Data of 9 Nights', '3rd order', 'fontweight','bold','fontsize',12 )
