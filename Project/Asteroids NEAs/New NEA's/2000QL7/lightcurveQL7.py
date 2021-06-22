import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('new light curve.csv')

fig, pd = plt.subplots(figsize=(10, 6))
pd.scatter(x=df['Phase'], y=df['Mag'], color="b",
           marker="+", s=40, label='5 Nights of Magnitude data')
pd.scatter(x=df['Phase'], y=df['Curve'], color='r', s=30, label='6th order curve')
plt.xlabel("Phase")
plt.ylabel("Magnitude")
plt.title('2000 QL7 Light Curve')
plt.legend(loc='upper right')
plt.gca().invert_yaxis()
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

plt.show()
fig.savefig('Final_light_curve 2000QL7.png', dpi=fig.dpi)
