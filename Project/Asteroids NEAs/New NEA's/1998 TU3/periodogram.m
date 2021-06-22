clear all;
close all;
clc;

% Import data from cvs file
data=csvread('periodogram log.csv', 2);
col1 = data(:, 1);
col2 = data(:, 2);

% Plotting the light curve
figure
plot(col1, col2)

title('1998 TU3 Periodogram', 'FontSize', 16)
xlabel('Period = 2.3777 Hours', 'fontweight','bold','fontsize',12)
ylabel('RMSE', 'fontweight','bold','fontsize',12)
% set(gca, 'ydir', 'reverse')
grid on
grid minor
% legend('Data of 5 Nights', '4th order', 'fontweight','bold','fontsize',12 )
