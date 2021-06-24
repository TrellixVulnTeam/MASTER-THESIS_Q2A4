import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import make_interp_spline

# plt.style.use('style/elegant.mplstyle')
df = pd.read_csv('new.csv')

fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(x=df['Phase'], y=df['Mag'], s=10, c='b', marker="+", label='3 Nights of Magnitude')
ax.scatter(x=df['Phase'], y=df['Curve'], s=10, c='r', label='4th order curve')
plt.gca().invert_yaxis()
plt.xlabel("Phase")
plt.ylabel("Magnitude")
plt.title('1998 TU3 Light Curve')
plt.legend(loc='best')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

plt.show()
fig.savefig('Final_light_curve_Ivar1627.png', dpi=fig.dpi)
