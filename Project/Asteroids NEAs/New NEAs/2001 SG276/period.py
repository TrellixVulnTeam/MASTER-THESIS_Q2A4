import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

if "setup_text_plots" not in globals():
    from astroML.plotting import setup_text_plots
setup_text_plots(fontsize=7, usetex=False)

df3 = pd.read_csv('/home/renetus/PycharmProjects/MASTER-THESIS/Project/Asteroids NEAs/New NEAs/2001 '
                  'SG276/periodogram.csv')
time = df3['Period(hours)'] * 24  # convert to hours
rmse = df3['RMSE']

fig, ax = plt.subplots()
fig.subplots_adjust(left=0.1, right=0.9, hspace=0.35)

# plot 1
plt.subplot(131)
plt.plot(time, rmse, '-k')
# ax.xlabel('Hours')
plt.ylabel('RMSE (x0.01 Mag)')
plt.ylim(3.8, 6.8)
plt.xlim(4.8, 5.5)
plt.minorticks_on()
plt.grid(b=True, which='major', color='gray', linestyle='-', linewidth=0.4)
plt.grid(b=True, which='minor', color='gray', linestyle='--', linewidth=0.2)
# plt.title('Periodogram: 2001 SG276', fontweight="bold", fontsize=16)
# plt.savefig('Periodogram: 2001 SG276 zoom.svg', dpi=1000)

# plot 2
ax1 = plt.subplot(132)
plt.plot(time, rmse, '-k')
plt.xlabel('Hours')
# plt.title('Periodogram: 2001 SG276')
# ax1.set_ylabel('RMSE (x0.01 Mag)')
ax1.axes.yaxis.set_ticklabels([])
plt.ylim(3.8, 6.8)
plt.xlim(7, 8)
plt.minorticks_on()
plt.grid(b=True, which='major', color='gray', linestyle='-', linewidth=0.4)
plt.grid(b=True, which='minor', color='gray', linestyle='--', linewidth=0.2)

# plot 3
ax = plt.subplot(133)
plt.plot(time, rmse, '-k')
# ax2.set_xlabel('Hours')
# ax1.ylabel('RMSE (x0.01 Mag)')
plt.ylim(3.8, 6.8)
plt.xlim(10, 11)
ax.axes.yaxis.set_ticklabels([])
plt.minorticks_on()
plt.grid(b=True, which='major', color='gray', linestyle='-', linewidth=0.4)
plt.grid(b=True, which='minor', color='gray', linestyle='--', linewidth=0.2)
plt.suptitle("Periodogram: 2001 SG276", fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig('RMSE comparison.svg', dpi=1000)
plt.show()
