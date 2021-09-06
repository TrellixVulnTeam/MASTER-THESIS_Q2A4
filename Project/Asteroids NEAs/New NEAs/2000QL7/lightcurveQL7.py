import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import make_interp_spline
import matplotlib

if "setup_text_plots" not in globals():
    from astroML.plotting import setup_text_plots
setup_text_plots(fontsize=15, usetex=True)
matplotlib.rcParams.update({'errorbar.capsize': 2})


df = pd.read_csv('new light curve.csv')
df3 = pd.read_csv('linear period.csv')
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

ax = df2.plot(x="Phase", y="Mag", kind="line", yerr="MagErr", title="Data", linestyle="", label='Data of 9 nights',
              marker="o", capthick=2, ecolor="dimgray", linewidth=1, figsize=(10, 6), zorder=1)
# ax = df2.plot(x="Phase", y="Mag", kind="scatter", yerr="MagErr", s=70, marker=".",
# label="Data of 5 nights", color="dimgray", figsize=(10, 6))
plt.plot(X_, Y_, color="C3", lw=3, label="Fit (3rd order)", zorder=2)
plt.xlabel("Phase [Period = 2.3750 H]")
plt.ylabel("$H_{g}$ [Mag]")
plt.title('2000 QL7 Light Curve', fontweight='bold', fontsize=21)
plt.legend(loc='best')
plt.gca().invert_yaxis()
plt.xlim(-0.1, 1.1)
plt.ylim(15.78, 15.36)
plt.minorticks_on()
plt.grid(b=True, which='major', color='gray', linestyle='-', linewidth=0.4)
# plt.grid(b=True, which='major', color='#666666', linestyle='-')
# plt.minorticks_on()
# plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
plt.savefig('Final_light_curve 2000QL7 new.svg', dpi=1000)

# plt.savefig('Final_light_curve 2000QL7.eps', format='eps', dpi=1000)


# def annot_max(time, rmse, ax=None):
#    xmax = time[np.argmin(rmse)]
#    ymax = rmse.min()
#    text = "Period={:.5f}, RMSE={:.5f}".format(xmax, ymax)
#    if not ax:
#        ax = plt.gca()
#    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
#    arrowprops = dict(arrowstyle="->", connectionstyle="angle")
#    kw = dict(xycoords='data', textcoords="axes fraction", arrowprops=arrowprops,
#              bbox=bbox_props, ha="right", va="bottom")
#    ax.annotate(text, xy=(xmax, ymax), xytext=(0.94, 0.96), **kw)


fig, ax = plt.subplots(figsize=(10, 6))

plt.plot(time, rmse, '-k')

# annot_max(time, rmse)
plt.xlabel('Hours')
plt.ylabel('RMSE (x0.01 Mag)')
# plt.xlim(2, 4)
plt.ylim(3.6, 6.0)
plt.xlim(2.1, 3.9)
plt.minorticks_on()
plt.grid(b=True, which='major', color='gray', linestyle='-', linewidth=0.4)
plt.grid(b=True, which='minor', color='gray', linestyle='--', linewidth=0.2)
plt.title('Periodogram: 2000 QL7', fontweight="bold", fontsize=21)
plt.savefig('Periodogram: 2000 QL7 zoom new.svg', dpi=1000)
plt.show()
