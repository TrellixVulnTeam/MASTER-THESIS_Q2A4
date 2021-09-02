import numpy as np
import matplotlib.pyplot as plt

# data to plot
t1 = [4.7964, 2.3750, 2.3777, 5.0906, 6.7970, 4.2739]  # light curves
t2 = [4.7950, 2.37512, 2.3750, 5.0900, 6.8020, 4.2736] # alcdef

# create plot
fig, ax = plt.subplots()
bar_width = 0.35
X = np.arange(6)

p1 = plt.bar(X, t1, bar_width, color='b',
label='ALCDEF')

# The bar of second plot starts where the first bar ends
p2 = plt.bar(X + bar_width, t2, bar_width,
color='g',
label='Light curve')

# plt.xlabel('Subject')
plt.ylabel('Period [Hours]')
plt.title('Rotation Period')
plt.xticks(X + (bar_width/2), ('Ivar', '2000QL7', '1998TU3', '2001SG276', '2001UY4', '2003RP8'))
plt.legend()

plt.tight_layout()
plt.show()