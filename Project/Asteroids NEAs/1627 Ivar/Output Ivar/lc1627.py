import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import make_interp_spline

# plt.style.use('style/elegant.mplstyle')
df = pd.read_csv('new.csv')
df3 = pd.read_csv('')
print(df)
df2 = df.sort_values(by="Phase")
print(df2)

time = df3['Period(hours)'] * 24  # convert to hours
rmse = df3['RMSE']

matplotlib.rcParams.update({'errorbar.capsize': 2})
ax = df2.plot(x="Phase", y="Mag", kind="line", yerr="MagErr", linestyle="",
              marker="o", label="Data of 3 nights", capthick=1, ecolor="dimgray",
              linewidth=1, figsize=(10, 6), zorder=1)
df2.plot(x="Phase", y="Curve", ax=ax, color="C3", lw=2, label="Fit (4th order)", zorder=2)

plt.gca().invert_yaxis()
plt.xlabel('Phase [Period = 4.7950 H')
plt.ylabel('Mag')
plt.title('IVAR Light Curve', fontweight='bold')
plt.legend(loc='best')
# plt.grid(b=True, which='major', color='#666666', linestyle='-')
# plt.minorticks_on()
# plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
plt.savefig('New_light_curve_Ivar1627.svg', dpi=1000)

# periodogram
fig, ax = plt.subplots(figsize=(10, 6))

plt.plot(time, rmse, '-k')
plt.xlabel('Hours')
plt.ylabel('RMSE')
plt.title('Periodogram: 2000 QL7', fontweight="bold", fontsize=16)
plt.savefig('Periodogram: Ivar1627.svg', dpi=1000)
plt.show()
plt.show()

