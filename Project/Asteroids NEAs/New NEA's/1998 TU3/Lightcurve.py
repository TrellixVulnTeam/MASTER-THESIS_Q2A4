import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import make_interp_spline

df = pd.read_csv('Light curve.csv')
print(df)

df2 = df.sort_values(by="Phase")
print(df2)

x = df2['Phase']
y = df2['Curve']
X_Y_Spline = make_interp_spline(x, y)
X_ = np.linspace(x.min(), x.max(), 500)
Y_ = X_Y_Spline(X_)

ax = df2.plot(x="Phase", y="Mag", kind="scatter", yerr="MagErr",
              s=70, marker=".", label="Data of 5 nights",
              color="gray", figsize=(10, 6))
plt.plot(X_, Y_, color="C3", lw=2, label="Fit (6th order)")

# ax.scatter(xdata, ydata, s=10, c='b', marker=".", label='5 Nights of Magnitude')
# ax = df.plot(x="Phase", y="Mag", kind="line", yerr="MagErr", linestyle="", marker=".",
# capthick=1, ecolor="gray", linewidth=1, label='5 nights of Magnitude')
# ax.scatter(x=df['Phase'], y=df['Curve'], s=10, c='r', label='6th order curve')
plt.gca().invert_yaxis()
plt.title('1998 TU3 Light Curve')
plt.legend(loc='best')
# plt.grid(b=True, which='major', color='#666666', linestyle='-')
# plt.minorticks_on()
# plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
plt.savefig('Final_light_curve_1998TU3.png', dpi=1000)
plt.show()
