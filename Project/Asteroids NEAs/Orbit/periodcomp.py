import numpy as np
import matplotlib.pyplot as plt

# data to plot
# t1 = [4.7964, 2.3750, 2.3777, 5.0906, 6.7970, 4.2739]  # light curves
# t2 = [4.7950, 2.37512, 2.3750, 5.0900, 6.8020, 4.2736]  # alcdef

a1 = [12.67, 15.61, 14.49, 17.81, 18.2, 18.2]
a2 = [12.9421, 15.555, 14.4118, 18.07277, 18.1931, 18.3856]
# create plot
fig, ax = plt.subplots()
bar_width = 0.30
X = np.arange(6)

p1 = plt.bar(X, a1, bar_width, color='k',
label='ALCDEF', zorder=3)

# The bar of second plot starts where the first bar ends
p2 = plt.bar(X + bar_width, a2, bar_width,
color='grey',
label='Light curve')

# plt.xlabel('Subject')
plt.ylim(10, 19)
plt.minorticks_on()
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=True)
plt.grid(zorder=0)
plt.grid(b=True, which='major', color='gray', linestyle='-', linewidth=0.4)
plt.grid(b=True, which='minor', color='gray', linestyle='--', linewidth=0.2)
plt.ylabel('Hg [mag]', fontweight='bold')
plt.title('Absolute Magnitude Hg', fontsize=14, fontweight='bold')
plt.xticks(X + (bar_width/2), ('Ivar', '2000QL7', '1998TU3', '2001SG276', '2001UY4', '2003RP8'), fontsize=8)
plt.legend()

plt.tight_layout()
plt.savefig('Hg comparison.svg', dpi=1000)
plt.show()
