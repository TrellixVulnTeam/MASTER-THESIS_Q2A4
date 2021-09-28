import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import make_interp_spline


if "setup_text_plots" not in globals():
    from astroML.plotting import setup_text_plots
setup_text_plots(fontsize=15, usetex=True)
# plt.style.use('seaborn-whitegrid')
df = pd.read_csv('light curve.csv')
df3 = pd.read_csv('periodogram log.csv')
# print(df)
df2 = df.sort_values(by="Phase")
# print(df2)

amp = df['Curve']
maxValue = max(amp)
minValue = min(amp)
av = [maxValue, minValue]
av2 = sum(av)/len(av)
print('Mean mag is ', av2)


def sub(num1, num2):
    return num1 - num2


print(maxValue)
print(minValue)
print('Amplitude is ', sub(maxValue, minValue))

x = df2['Phase']
y = df2['Curve']
time = df3['Period(hours)'] * 24  # convert to hours
rmse = df3['RMSE']

X_Y_Spline = make_interp_spline(x, y)
X_ = np.linspace(x.min(), x.max(), 500)
Y_ = X_Y_Spline(X_)

matplotlib.rcParams.update({'errorbar.capsize': 2})
ax = df2.plot(x="Phase", y="Mag", kind="line", yerr="MagErr", linestyle="",
              marker="o", label="Data of 4 nights", capthick=1, ecolor="dimgray",
              linewidth=1, figsize=(10, 6), zorder=1)
plt.plot(X_, Y_, color="C3", lw=3, label="Fit (6th order)", zorder=2)
plt.gca().invert_yaxis()
plt.minorticks_on()
plt.grid(b=True, which='major', color='gray', linestyle='-', linewidth=0.4)
plt.xlim(-0.1, 1.1)
plt.ylim(18.34, 18.01)
plt.xlabel("Phase [Period = 6.7970 H]")
plt.ylabel("$H_{g}$ [Mag]")
plt.title('2001 UY4 Light Curve', fontweight="bold", fontsize=21)
plt.legend(loc='best')
# plt.grid(b=True, which='major', color='#666666', linestyle='-')
# plt.minorticks_on()
# plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
plt.savefig('New_light_curve_2001UY4 new.svg', dpi=1000)

# periodogram
fig, ax = plt.subplots(figsize=(10, 6))

plt.plot(time, rmse, '-k', linewidth=2.0)
plt.minorticks_on()
plt.grid(b=True, which='major', color='gray', linestyle='-', linewidth=0.4)
plt.grid(b=True, which='minor', color='gray', linestyle='--', linewidth=0.2)
plt.xlabel('Hours')
plt.ylabel('RMSE (x0.01 Mag)')
plt.xlim(4, 8)
# plt.xlim(0, 13)  # plt.xlim(4, 6)
plt.ylim(1.2, 5.4)
plt.title('Periodogram Log: 2001 UY4', fontweight="bold", fontsize=21)
plt.savefig('Periodogram: 2001UY4 zoom new.svg', dpi=1000)
plt.show()