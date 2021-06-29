import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import make_interp_spline
import matplotlib

matplotlib.rcParams.update({'errorbar.capsize': 2})

df = pd.read_csv('new light curve.csv')
print(df)
df2 = df.sort_values(by="Phase")
print(df2)

x = df2['Phase']
y = df2['Curve']
X_Y_Spline = make_interp_spline(x, y)
X_ = np.linspace(x.min(), x.max(), 500)
Y_ = X_Y_Spline(X_)

ax = df2.plot(x="Phase", y="Mag", kind="line", yerr="MagErr", title="Data", linestyle="", label='Data of 9 nights',
              marker="o", capthick=2, ecolor="dimgray", linewidth=1, figsize=(10, 6), zorder=1)
# ax = df2.plot(x="Phase", y="Mag", kind="scatter", yerr="MagErr", s=70, marker=".",
# label="Data of 5 nights", color="dimgray", figsize=(10, 6))
plt.plot(X_, Y_, color="C3", lw=3, label="Fit (3rd order)", zorder=2)
plt.xlabel("Phase [Period = 2.3750 H]")
plt.ylabel("Mag")
plt.title('2000 QL7 Light Curve', fontweight='bold')
plt.legend(loc='upper right')
plt.gca().invert_yaxis()
# plt.grid(b=True, which='major', color='#666666', linestyle='-')
# plt.minorticks_on()
# plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
plt.savefig('Final_light_curve 2000QL7.png', dpi=1000)
# plt.savefig('Final_light_curve 2000QL7.eps', format='eps', dpi=1000)
plt.show()
