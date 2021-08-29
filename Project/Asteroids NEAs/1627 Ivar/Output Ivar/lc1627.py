import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.legend import Legend
from scipy.interpolate import make_interp_spline

plt.style.use('seaborn-whitegrid')
matplotlib.rcParams.update({'errorbar.capsize': 2})
# Import raw data from csv file
df1 = pd.read_csv('raw.csv')
print(df1)

ax = df1.plot(x="JD", y="Mag", kind="line", yerr="MagErr", linestyle="",
              marker="o", label="Data of 3 nights", capthick=1, ecolor="dimgray",
              linewidth=1, figsize=(10, 6), zorder=1)
plt.gca().invert_yaxis()
plt.xlabel('JD')
plt.ylabel('Mag')
plt.title('IVAR rawplot', fontweight='bold')
plt.legend(loc='best')

# Import raw data from alcdef dataset
df4 = pd.read_csv('raw plot 3.csv')

matplotlib.rcParams.update({'errorbar.capsize': 2})
ax = df4.plot(x="JD", y="Mag", kind="line", yerr="MagErr", linestyle="",
              marker="o", label="Data of 4 nights", capthick=1, ecolor="dimgray",
              linewidth=1, figsize=(10, 6), zorder=1)
plt.gca().invert_yaxis()
plt.xlabel('JD')
plt.ylabel('Mag')
plt.title('IVAR rawplot (alcdef)', fontweight='bold')
plt.legend(loc='best')

# Import csv data of Ivar from FITS dataset
df = pd.read_csv('new.csv')
df3 = pd.read_csv('period.csv')
print(df)
df2 = df.sort_values(by="Phase")
print(df2)

amp = df['Curve']
maxValue = max(amp)
minValue = min(amp)


def sub(num1, num2):
    return num1 - num2


print(maxValue)
print(minValue)
print('Amplitude is ', sub(maxValue, minValue))

time = df3['Period(hours)']  # convert to hours
rmse = df3['RMSE']

ax = df2.plot(x="Phase", y="Mag", kind="line", yerr="MagErr", linestyle="",
              marker="o", label="Data of 3 nights", capthick=1, ecolor="dimgray",
              linewidth=1, figsize=(10, 6), zorder=1)
df2.plot(x="Phase", y="Curve", ax=ax, color="C3", lw=2, label="Fit (4th order)", zorder=2)

plt.gca().invert_yaxis()
plt.xlabel('Phase [Period = 4.79640 H]')
plt.ylabel('Mag')
plt.title('IVAR Light Curve', fontweight='bold')
plt.legend(loc='best')
# plt.grid(b=True, which='major', color='#666666', linestyle='-')
# plt.minorticks_on()
# plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
plt.savefig('New_light_curve_Ivar1627.svg', dpi=1000)

# import Ivar from dataset
df5 = pd.read_csv('lc without fits.csv')
df5a = df5.sort_values(by="Phase")

ax = df5.plot(x="Phase", y="Mag", kind="line", yerr="MagErr", linestyle="",
              marker="o", label="Data of 4 nights", capthick=1, ecolor="dimgray",
              linewidth=1, figsize=(10, 6), zorder=1)
df5a.plot(x="Phase", y="Curve", ax=ax, color="C3", lw=2, label="Fit (4th order)", zorder=2)

plt.gca().invert_yaxis()
plt.xlabel('Phase [Period = 4.7965 H]')
plt.ylabel('Mag')
plt.title('IVAR Light Curve (alcdef)', fontweight='bold')
plt.legend(loc='best')

plt.savefig('LightCurve_Ivar1627_(alcdef).svg', dpi=1000)
# periodogram
fig, ax = plt.subplots(figsize=(10, 6))

plt.plot(time, rmse, '-k')
plt.xlabel('Hours')
plt.ylabel('RMSE (x0.01 Mag)')
plt.title('Periodogram: Ivar 1627', fontweight="bold", fontsize=16)
plt.savefig('Periodogram: Ivar1627.svg', dpi=1000)

# zoom plot
plt.xlabel('Hours')
plt.ylabel('RMSE (x0.01 Mag)')
plt.xlim(2, 6)
plt.title('Periodogram: Ivar 1627', fontweight="bold", fontsize=16)
plt.savefig('Periodogram: Ivar 1627 zoom.svg', dpi=1000)
plt.show()
