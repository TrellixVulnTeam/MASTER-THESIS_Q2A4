import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.legend import Legend
from scipy.interpolate import make_interp_spline

if "setup_text_plots" not in globals():
    from astroML.plotting import setup_text_plots
setup_text_plots(fontsize=15, usetex=True)

matplotlib.rcParams.update({'errorbar.capsize': 2})
# Import raw data from csv file
df1 = pd.read_csv('raw.csv')
# print(df1)

# ax = df1.plot(x="JD", y="Mag", kind="line", yerr="MagErr", linestyle="",
#               marker="o", label="Data of 3 nights", capthick=1, ecolor="dimgray",
#               linewidth=1, figsize=(10, 6), zorder=1)
# plt.gca().invert_yaxis()
# plt.xlabel('JD')
# plt.ylabel('Mag')
# plt.title('IVAR rawplot', fontweight='bold')
# plt.legend(loc='best')

# Import raw data from alcdef dataset
# df4 = pd.read_csv('raw plot 3.csv')
#
# matplotlib.rcParams.update({'errorbar.capsize': 2})
# ax = df4.plot(x="JD", y="Mag", kind="line", yerr="MagErr", linestyle="",
#               marker="o", label="Data of 4 nights", capthick=1, ecolor="dimgray",
#               linewidth=1, figsize=(10, 6), zorder=1)
# plt.gca().invert_yaxis()
# plt.xlabel('JD')
# plt.ylabel('Mag')
# plt.title('IVAR rawplot (alcdef)', fontweight='bold')
# plt.legend(loc='best')

# Import csv data of Ivar from FITS dataset
df = pd.read_csv('new.csv')
df3 = pd.read_csv('period.csv')
print(df)
df2 = df.sort_values(by="Phase")
print(df2)

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


time = df3['Period(hours)']  # convert to hours
rmse = df3['RMSE']

# ax = df2.plot(x="Phase", y="Mag", kind="line", yerr="MagErr", linestyle="",
#               marker="o", label="Data of 3 nights", capthick=1, ecolor="dimgray",
#               linewidth=1, figsize=(10, 6), zorder=1)
# df2.plot(x="Phase", y="Curve", ax=ax, color="C3", lw=2, label="Fit (4th order)", zorder=2)
ax = df2.plot(x="Phase", y="Mag", yerr="MagErr", fmt='.k', ecolor='gray',
            lw=1, ms=4, capsize=1.5, alpha=0.3, figsize=(10, 6))
df2.plot(x="Phase", y="Curve", ax=ax, markeredgecolor='b', lw=2, fillstyle='top', linestyle='solid',label="Fit ("
                                                                                                          "$4th order)")

plt.gca().invert_yaxis()
plt.xlabel('Phase [Period = 4.79640 H]')
plt.ylabel('$H_{g}$ [Mag]')
plt.title('IVAR Light Curve', fontweight='bold', fontsize=21)
plt.xlim(-0.1, 1.1)
plt.ylim(13.66, 12.29)
plt.minorticks_on()
plt.grid(b=True, which='major', color='gray', linestyle='-', linewidth=0.4)
plt.legend(loc='best')
# plt.grid(b=True, which='major', color='#666666', linestyle='-')
# plt.minorticks_on()
# plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
plt.savefig('New_light_curve_Ivar1627.svg', dpi=1000)

# import Ivar from dataset
# df5 = pd.read_csv('lc without fits.csv')
# df5a = df5.sort_values(by="Phase")
#
# ax = df5.plot(x="Phase", y="Mag", kind="line", yerr="MagErr", linestyle="",
#               marker="o", label="Data of 4 nights", capthick=1, ecolor="dimgray",
#               linewidth=1, figsize=(10, 6), zorder=1)
# df5a.plot(x="Phase", y="Curve", ax=ax, color="C3", lw=2, label="Fit (4th order)", zorder=2)
#
# plt.gca().invert_yaxis()
# plt.xlabel('Phase [Period = 4.7965 H]')
# plt.ylabel('$H_{g}$ [Mag]')
# plt.title('IVAR Light Curve (alcdef)', fontweight='bold')
# plt.legend(loc='best')
#
# plt.savefig('LightCurve_Ivar1627_(alcdef).svg', dpi=1000)
# periodogram
fig, ax = plt.subplots(figsize=(9, 6))


# plt.xlabel('Hours')
# plt.ylabel('RMSE (x0.01 Mag)')
# plt.minorticks_on()
# plt.grid(b=True, which='major', color='gray', linestyle='-', linewidth=0.4)
# plt.grid(b=True, which='minor', color='gray', linestyle='--', linewidth=0.2)
# plt.title('Periodogram: Ivar 1627', fontweight="bold", fontsize=16)
# plt.savefig('Periodogram: Ivar1627 new.svg', dpi=1000)

# zoom plot
# plt.xlabel('Hours')
# plt.ylabel('RMSE (x0.01 Mag)')
# plt.xlim(0, 13)
# plt.ylim(3, 38)
# plt.minorticks_on()
# plt.grid(b=True, which='major', color='gray', linestyle='-', linewidth=0.4)
# plt.grid(b=True, which='minor', color='gray', linestyle='--', linewidth=0.2)
# plt.title('Periodogram: Ivar 1627', fontweight="bold", fontsize=21)
# plt.savefig('Periodogram: Ivar 1627 new.svg', dpi=1000)
# plt.show()

fig.subplots_adjust(left=0.1, right=0.9, hspace=0.35)


# plot 1
plt.subplot(121)
plt.plot(time, rmse, '-k', linewidth=2)
# ax.xlabel('Hours')
plt.ylabel('RMSE (x0.01 Mag)')
plt.ylim(3, 38)
plt.xlim(2.1, 2.9)
plt.minorticks_on()
plt.grid(b=True, which='major', color='gray', linestyle='-', linewidth=0.4)
plt.grid(b=True, which='minor', color='gray', linestyle='--', linewidth=0.2)
# plt.title('Periodogram: 2001 SG276', fontweight="bold", fontsize=16)
# plt.savefig('Periodogram: 2001 SG276 zoom.svg', dpi=1000)

# plot 2
ax1 = plt.subplot(122)
plt.plot(time, rmse, '-k', linewidth=2)

# plt.title('Periodogram: 2001 SG276')
# ax1.set_ylabel('RMSE (x0.01 Mag)')
ax1.axes.yaxis.set_ticklabels([])
plt.ylim(3, 38)
plt.xlim(4.3, 5.1)
plt.minorticks_on()
plt.grid(b=True, which='major', color='gray', linestyle='-', linewidth=0.4)
plt.grid(b=True, which='minor', color='gray', linestyle='--', linewidth=0.2)
fig.supxlabel('Hours')
plt.suptitle("Periodogram: Ivar 1627", fontsize=21, fontweight='bold')
plt.savefig('Periodogram: 1627 zoom.svg', dpi=1000)
plt.show()
