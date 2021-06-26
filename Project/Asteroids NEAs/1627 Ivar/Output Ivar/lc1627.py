import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import make_interp_spline

# plt.style.use('style/elegant.mplstyle')
df = pd.read_csv('new.csv')
print(df)
df2 = df.sort_values(by="Phase")
print(df2)

ax = df2.plot(x="Phase", y="Mag", kind="scatter", yerr="MagErr", s=50,
              color="dimgray", marker=".", label="Data of 5 nights", figsize=(10, 6))
df2.plot(x="Phase", y="Curve", ax=ax, color="C3", lw=2, label="Fit (4th order)")

plt.gca().invert_yaxis()
plt.title('IVAR Light Curve', fontweight='bold')
plt.legend(loc='best')
# plt.grid(b=True, which='major', color='#666666', linestyle='-')
# plt.minorticks_on()
# plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
plt.savefig('New_light_curve_Ivar1627.png', dpi=1000)
plt.show()

