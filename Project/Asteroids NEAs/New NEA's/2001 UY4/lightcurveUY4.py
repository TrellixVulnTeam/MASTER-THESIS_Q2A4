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

ax = df2.plot(x="Phase", y="Mag", kind="scatter", yerr="MagErr",
              s=70, marker=".", label="Data of 4 nights",
              color="dimgray", figsize=(10, 6))
plt.plot(X_, Y_, color="C3", lw=2, label="Fit (6th order)")
plt.gca().invert_yaxis()
plt.xlabel("Phase")
plt.ylabel("Mag")
plt.title('2001 UY4 Light Curve', fontweight="bold")
plt.legend(loc='best')
# plt.grid(b=True, which='major', color='#666666', linestyle='-')
# plt.minorticks_on()
# plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
plt.savefig('New_light_curve_2001UY4.png', dpi=1000)
plt.show()
