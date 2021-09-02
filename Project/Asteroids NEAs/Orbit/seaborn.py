import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

if "setup_text_plots" not in globals():
    from astroML.plotting import setup_text_plots
setup_text_plots(fontsize=7, usetex=False)
# sns.set_theme(style="ticks")

N = 6
dy = 0.1 + 0.1 * np.random.random(N)
dy2 = 0.07 + 0.07 * np.random.random(N)
x = [1, 2, 3, 4, 5, 6]
n = ['Ivar', '2000QL7', '1998TU3', '2001SG276', '2001UY4', '2003RP8']
# y = [0.399826, 0.505526, 0.484694, 0.251227, 0.786435, 0.374033]  # eccentricity
# y2 = [8.47739, 17.7793, 5.40318, 26.555, 5.43401, 31.2261]      # inclination
# y3 = [133.2, 338.305, 102.217, 34.8889, 160.812, 301.517]  # Ascending node
# y4 = [167.666, 100.62, 85.17, 201.278, 107.691, 21.6902] # Argument of perigee
# y5 = [283.095, 53.376, 179.32, 310.426, 133.091, 355.737]  # true anomaly
# y6 = [1.86157, 2.41123, 0.788684, 1.43109, 1.4563, 1.74509]  # semi-major axis
# y7 = [1.11727, 1.19229, 0.406414, 1.07156, 0.311013, 1.09237]  # periapsis
y8 = [2.52773, 3.72621, 0.697052, 1.70377, 1.74898, 2.29423]  # period in years
y9 = [4.7964, 2.3750, 2.3777, 5.0906, 6.7970, 4.2739]
fig = plt.figure(figsize=(5, 3.75))
fig.subplots_adjust(left=0.1, right=0.9, hspace=0.35)

# First panel: the data
ax = fig.add_subplot(211)
ax.errorbar(x, y9, dy, fmt='.k', lw=1, ecolor='gray')
# plt.plot(x, y, color='dimgray', linestyle='dashed', linewidth=0.5,
#          marker='.', markerfacecolor='black', markersize=12)
for i, txt in enumerate(n):
    ax.annotate(txt, (x[i], y9[i]), xytext=(x[i], y9[i] + 0.4), ha='center')
ax.set_ylim(1, 8)
ax.set_xlim(0.5, 6.5)
ax.minorticks_on()
ax.grid(b=True, which='major', color='gray', linestyle='-', linewidth=0.4)
ax.grid(b=True, which='minor', color='gray', linestyle='--', linewidth=0.2)
ax.set_ylabel('Period [hours]', fontsize=8)
ax.axes.get_xaxis().set_visible(False)
ax.set_title('Rotation Period Comparison', fontsize=9, fontweight='bold')

# Second panel: the periodogram & significance levels
ax1 = fig.add_subplot(212)
ax1.errorbar(x, y8, dy2, fmt='.k', lw=1, ecolor='gray')
# ax1.plot(x, y6, color='dimgray', linestyle='dashed', linewidth=0.5,
#          marker='.', markerfacecolor='black', markersize=12)
for i, txt in enumerate(n):
    ax1.annotate(txt, (x[i], y8[i]), xytext=(x[i], y8[i] + 0.3), ha='center')
ax1.set_ylim(0, 4.44)
ax1.set_xlim(0.5, 6.5)
ax1.minorticks_on()
ax1.grid(b=True, which='major', color='gray', linestyle='-', linewidth=0.4)
ax1.grid(b=True, which='minor', color='gray', linestyle='--', linewidth=0.2)
ax1.set_ylabel('Period [years]', fontsize=8)
ax1.set_title('Orbit Period Comparison', fontsize=9, fontweight='bold')
ax1.axes.get_xaxis().set_visible(False)

plt.savefig('h and t comparison.svg', dpi=1000)
plt.show()
