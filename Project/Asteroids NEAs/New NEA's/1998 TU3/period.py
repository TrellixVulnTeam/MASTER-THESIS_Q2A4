import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from astropy.timeseries import LombScargle
from scipy.interpolate import make_interp_spline
from gatspy.periodic import LombScargleFast
import seaborn

seaborn.set()

df = pd.read_csv('Light curve.csv')
print(df)

df2 = df.sort_values(by="Phase")
print(df2)
t = df2['Phase']
mag = df2['Mag']
dmag = df2['MagErr']

fig, ax = plt.subplots()
ax.errorbar(t, mag, dmag, fmt='.k', ecolor='gray')
ax.set(xlabel='Phase', ylabel='mag',
       title='Raw plot of 1998 TU3')
ax.invert_yaxis()
plt.show()

model = LombScargleFast().fit(t, mag, dmag)
periods, power = model.periodogram_auto(nyquist_factor=100)

fig, ax = plt.subplots()

ax.plot(periods, power)
ax.set(xlim=(0.0, 0.5), ylim=(0.0, 0.8),
       xlabel='period (days)',
       ylabel='Lomb-Scargle Power')
plt.show()

# set range and find period
#model.optimizer.period_range = (0.0, 0.1)
#period = model.best_period
#print("period = {0}".format(period))
