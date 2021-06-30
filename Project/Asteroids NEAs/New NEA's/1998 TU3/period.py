import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from astropy.timeseries import LombScargle
from scipy.interpolate import make_interp_spline
from gatspy.periodic import LombScargleFast

plt.style.use('seaborn-whitegrid')
df = pd.read_csv('Light curve.csv')
df3 = pd.read_csv('periodogram log.csv')
print(df)

df2 = df.sort_values(by="Phase")
print(df2)
t = df2['Phase']
mag = df2['Mag']
dmag = df2['MagErr']
y = df2['Curve']
time = df3['Period(hours)'] * 24  # convert to hours
rmse = df3['RMSE']
y_obs = np.random.normal(mag, dmag)

X_Y_Spline = make_interp_spline(t, y)
X_ = np.linspace(t.min(), t.max(), 500)
Y_ = X_Y_Spline(X_)

fig, ax = plt.subplots(figsize=(10, 6))
ax.errorbar(t, mag, dmag, fmt='.k', ecolor='gray')
ax.plot(t, y, '-k')
ax.set(xlabel='Phase', ylabel='Mag',
       title='Raw plot of 1998 TU3')
ax.invert_yaxis()

fig, ax = plt.subplots(figsize=(10, 6))
plt.plot(time, rmse, '-k')
plt.xlabel('Hours')
plt.ylabel('RMSE')
plt.title('Periodogram: 1998 TU3', fontweight="bold", fontsize=16)
plt.savefig('Periodogram: 1998 TU3.svg', dpi=1000)
# plt.show()

model = LombScargleFast().fit(t, mag, dmag)
periods, power = model.periodogram_auto(nyquist_factor=100)

fig, ax = plt.subplots()

ax.plot(periods, power, '-k')
ax.set(xlim=(0.0, 0.1), ylim=(-0.0, 0.8),
       xlabel='period (days)',
       ylabel='Lomb-Scargle Power')
plt.show()

# set range and find period
model.optimizer.period_range = (0.0, 1.0)
period = model.best_period
print("period = {0}".format(period))
