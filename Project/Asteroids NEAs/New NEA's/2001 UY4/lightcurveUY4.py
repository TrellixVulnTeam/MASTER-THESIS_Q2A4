import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import make_interp_spline

df = pd.read_csv('light curve.csv')
print(df)
df2 = df.sort_values(by="Phase")
print(df2)
x = df2['Phase']
y = df2['Curve']
X_Y_Spline = make_interp_spline(x, y)
X_ = np.linspace(x.min(), x.max(), 500)
Y_ = X_Y_Spline(X_)

matplotlib.rcParams.update({'errorbar.capsize': 2})
ax = df2.plot(x="Phase", y="Mag", kind="line", yerr="MagErr", linestyle="",
              marker="o", label="Data of 4 nights", capthick=1, ecolor="dimgray",
              linewidth=1, figsize=(10, 6), zorder=1)
plt.plot(X_, Y_, color="C3", lw=3, label="Fit (6th order)", zorder=2)
plt.gca().invert_yaxis()
plt.xlabel("Phase [Period = 6.7970 H")
plt.ylabel("Mag")
plt.title('2001 UY4 Light Curve', fontweight="bold")
plt.legend(loc='best')
# plt.grid(b=True, which='major', color='#666666', linestyle='-')
# plt.minorticks_on()
# plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
plt.savefig('New_light_curve_2001UY4.png', dpi=1000)
plt.show()
