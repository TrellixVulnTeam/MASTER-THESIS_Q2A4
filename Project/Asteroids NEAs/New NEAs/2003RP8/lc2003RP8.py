import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

# plt.style.use('seaborn-whitegrid')
if "setup_text_plots" not in globals():
    from astroML.plotting import setup_text_plots
setup_text_plots(fontsize=15, usetex=True)

matplotlib.rcParams.update({'errorbar.capsize': 2})
df = pd.read_csv('2003RP8.csv')
df3 = pd.read_csv('Periodogram.csv')
# print(df)
df2 = df.sort_values(by="Phase")
# print(df2)

amp = df['Curve']
maxValue = max(amp)
minValue = min(amp)
av = [maxValue, minValue]
av2 = sum(av)/len(av)
print('Mean mag is ', av2)


def sub(num1, num2):
    return num1 - num2


print(maxValue)
print(minValue)
print('Amplitude is ', sub(maxValue, minValue))

ax = df2.plot(
    x="Phase", y="Mag",
    kind="line", yerr="MagErr",
    linestyle="", marker="o", label='Data of 5 nights',
    capthick=1, ecolor="dimgray", linewidth=1, figsize=(10, 6), zorder=1
)  # figsize=(10, 6)
# ax = df2.plot(x="Phase", y="Mag", kind="scatter", yerr="MagErr", s=70,
#              color="dimgray", marker=".", label="Data of 5 nights", figsize=(10, 6))
df2.plot(x="Phase", y="Curve", ax=ax, color="C3", lw=3, label="Fit (6th order)", zorder=2)
plt.xlim(-0.1, 1.1)
plt.ylim(18.05, 18.85)
plt.gca().invert_yaxis()
plt.minorticks_on()
plt.grid(b=True, which='major', color='gray', linestyle='-', linewidth=0.4)
plt.xlabel('Phase [Period = 4.2739 H]')
plt.ylabel('$H_{g}$ [Mag]')
plt.title('2003 RP8 Light Curve', fontweight="bold", fontsize=16)
plt.legend(loc='upper center')
# plt.grid(b=True, which='major', color='#666666', linestyle='-')
# plt.minorticks_on()
# plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
plt.savefig('New_light_curve_2003RP8.svg', dpi=1200)

# periodogram
time = df3['Period(hours)'] * 24  # convert to hours
rmse = df3['RMSE']

fig, ax = plt.subplots(figsize=(10, 7))

plt.plot(time, rmse, '-k', linewidth=2.0)
plt.xlabel('Hours')
plt.ylabel('RMSE (x0.01 Mag)')
plt.xlim(0, 13)  # plt.xlim(4, 6)
plt.ylim(0.2, 17.8)
plt.minorticks_on()
plt.grid(b=True, which='major', color='gray', linestyle='-', linewidth=0.4)
plt.grid(b=True, which='minor', color='gray', linestyle='--', linewidth=0.2)
plt.title('Periodogram: 2003 RP8', fontweight="bold", fontsize=21)
plt.savefig('Periodogram: 2003RP8 new.svg', dpi=1000)
plt.show()
