import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import make_interp_spline
import matplotlib


matplotlib.rcParams.update({'errorbar.capsize': 2})

df = pd.read_csv('Light curve.csv')
print(df)

df2 = df.sort_values(by="Phase")
print(df2)

x = df2['Phase']
y = df2['Curve']
X_Y_Spline = make_interp_spline(x, y)
X_ = np.linspace(x.min(), x.max(), 500)
Y_ = X_Y_Spline(X_)

ax = df2.plot(x="Phase", y="Mag", kind="line", yerr="MagErr", linestyle="",
              marker="o", label="Data of 5 nights", capthick=1, ecolor="dimgray",
              linewidth=1, figsize=(10, 6), zorder=1)
plt.plot(X_, Y_, color="C3", lw=3, label="Fit (6th order)", zorder=2)

# ax.scatter(xdata, ydata, s=10, c='b', marker=".", label='5 Nights of Magnitude')
# ax = df.plot(x="Phase", y="Mag", kind="line", yerr="MagErr", linestyle="", marker=".",
# capthick=1, ecolor="gray", linewidth=1, label='5 nights of Magnitude')
# ax.scatter(x=df['Phase'], y=df['Curve'], s=10, c='r', label='6th order curve')
plt.xlabel("Phase [Period = 2.3777 H]")
plt.ylabel("Mag")
plt.gca().invert_yaxis()
plt.title('1998 TU3 Light Curve')
plt.legend(loc='best')
# plt.grid(b=True, which='major', color='#666666', linestyle='-')
# plt.minorticks_on()
# plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
plt.savefig('Final_light_curve_1998TU3.png', dpi=1000)
plt.show()
