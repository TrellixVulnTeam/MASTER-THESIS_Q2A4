import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('2003RP8.csv')
print(df)
df2 = df.sort_values(by="Phase")
print(df2)

ax = df2.plot(x="Phase", y="Mag", kind="scatter", yerr="MagErr", s=70,
              color="dimgray", marker=".", label="Data of 5 nights", figsize=(10, 6))
df2.plot(x="Phase", y="Curve", ax=ax, color="C3", lw=3, label="Fit (6th order)")

plt.gca().invert_yaxis()
plt.title('2003 RP8 Light Curve', fontweight='bold')
plt.legend(loc='upper center')
# plt.grid(b=True, which='major', color='#666666', linestyle='-')
# plt.minorticks_on()
# plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
plt.savefig('New_light_curve_2003RP8.png', dpi=1200)
plt.show()
