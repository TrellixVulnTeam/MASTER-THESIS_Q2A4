import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import make_interp_spline
import matplotlib

if "setup_text_plots" not in globals():
    from astroML.plotting import setup_text_plots
setup_text_plots(fontsize=15, usetex=True)

matplotlib.rcParams.update({'errorbar.capsize': 2})

# phase data import
df = pd.read_csv('Light curve.csv')
# print(df)
# df['Mag'].plot()
# df['Mag'].rolling(window=20).mean().plot()

df2 = df.sort_values(by="Phase")
# print(df2)

amp = df['Curve']
maxValue = max(amp)
minValue = min(amp)
av = [maxValue, minValue]
av2 = sum(av) / len(av)
print('Mean mag is ', av2)


def sub(num1, num2):
    return num1 - num2


print(maxValue)
print(minValue)
print('Amplitude is ', sub(maxValue, minValue))
x = df2['Phase']
y = df2['Curve']
X_Y_Spline = make_interp_spline(x, y)
X_ = np.linspace(x.min(), x.max(), 500)
Y_ = X_Y_Spline(X_)

# ax = df2.plot(x="Phase", y="Mag", kind="line", yerr="MagErr", linestyle="",
#               marker="o", label="Data of 5 nights", capthick=1, ecolor="dimgray",
#               linewidth=1, figsize=(10, 6), zorder=1)
# plt.plot(X_, Y_, color="C3", lw=3, label="Fit (4th order)", zorder=2)
ax = df2.plot(x="Phase", y="Mag", yerr="MagErr", fmt='.k', ecolor='gray',
              lw=1.5, ms=8, capsize=2.5, alpha=0.6, figsize=(10, 6), zorder=0)
plt.plot(X_, Y_, markeredgecolor='b', lw=2.5, fillstyle='top', linestyle='solid',
         label="Fit (4th order)", zorder=2)
# ax.scatter(xdata, ydata, s=10, c='b', marker=".", label='5 Nights of Magnitude')
# ax = df.plot(x="Phase", y="Mag", kind="line", yerr="MagErr", linestyle="", marker=".",
# capthick=1, ecolor="gray", linewidth=1, label='5 nights of Magnitude')
# ax.scatter(x=df['Phase'], y=df['Curve'], s=10, c='r', label='6th order curve')
plt.xlabel("Phase [Period = 2.3777 H]")
plt.ylabel("$H_{g}$ [Mag]")
plt.gca().invert_yaxis()
plt.xlim(-0.1, 1.1)
plt.ylim(14.49, 14.31)
plt.minorticks_on()
plt.grid(b=True, which='major', color='gray', linestyle='-', linewidth=0.4)
plt.title('1998 TU3 Light Curve', fontweight="bold", fontsize=21)
plt.legend(loc='best')
# plt.grid(b=True, which='major', color='#666666', linestyle='-')
# plt.minorticks_on()
# plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
plt.savefig('Final_light_curve_1998TU3 new.svg', dpi=1000)

# period data import
df3 = pd.read_csv('periodogram log.csv')

time = df3['Period(hours)'] * 24  # convert to hours
rmse = df3['RMSE']

fig, ax = plt.subplots(figsize=(10, 6))

plt.plot(time, rmse, '-k')

# def annot_max(time, rmse, ax=None):
#    xmax = time[np.argmin(rmse)]
#    ymax = rmse.min()
#    text = "Period={:.5f}".format(xmax, ymax)
#    if not ax:
#        ax = plt.gca()
#    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
#    arrowprops = dict(arrowstyle="->")
#    kw = dict(xycoords='data', textcoords="offset points",
#              arrowprops={}, bbox=bbox_props)
#    ax.annotate(text, xy=(xmax, ymax), xytext=(0.94, 0.96), **kw)


# annot_max(time, rmse)

# plt.plot(time, rmse, '-k')
# plt.xlabel('Hours')
# plt.ylabel('RMSE (x0.01 Mag)')
# plt.title('Periodogram: 1998 TU3', fontweight="bold", fontsize=21)
# # plt.savefig('Periodogram: 1998 TU3.svg', dpi=1000)

# zoom
plt.xlabel('Hours')
plt.ylabel('RMSE (x0.01 Mag)')
plt.xlim(2.1, 3.9)
plt.ylim(1.49, 3.0)
plt.minorticks_on()
plt.grid(b=True, which='major', color='gray', linestyle='-', linewidth=0.4)
plt.grid(b=True, which='minor', color='gray', linestyle='--', linewidth=0.2)
plt.title('Periodogram: 1998 TU3', fontweight="bold", fontsize=21)
plt.savefig('Periodogram: 1998 TU3 new zoom.svg', dpi=1000)

plt.show()
