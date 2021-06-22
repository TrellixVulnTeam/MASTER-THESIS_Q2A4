import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Light curve.csv')

fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(x=df['Phase'], y=df['Mag'], s=10, c='b', marker="+", label='5 Nights of Magnitude')
ax.scatter(x=df['Phase'], y=df['Curve'], s=10, c='r', label='6th order curve')
plt.gca().invert_yaxis()
plt.xlabel("Phase")
plt.ylabel("Magnitude")
plt.title('1998 TU3 Light Curve')
plt.legend(loc='best')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

plt.show()
fig.savefig('Final_light_curve_1998TU3.png', dpi=fig.dpi)
