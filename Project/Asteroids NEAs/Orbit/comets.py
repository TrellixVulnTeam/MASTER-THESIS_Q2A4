from skyfield.api import load
from skyfield.data import mpc

with load.open(mpc.COMET_URL) as f:
    comets = mpc.load_comets_dataframe(f)

print(len(comets), 'comets loaded')

# Keep only the most recent orbit for each comet,
# and index by designation for fast lookup.
comets = (comets.sort_values('reference')
          .groupby('designation', as_index=False).last()
          .set_index('designation', drop=False))

# Sample lookups.
row = comets.loc['1P/Halley']
row = comets.loc['C/1995 O1 (Hale-Bopp)']

# Generating a position.

from skyfield.constants import GM_SUN_Pitjeva_2005_km3_s2 as GM_SUN

ts = load.timescale()
eph = load('de421.bsp')
sun, earth = eph['sun'], eph['earth']

comet = sun + mpc.comet_orbit(row, ts, GM_SUN)

t = ts.utc(2020, 5, 31)
ra, dec, distance = earth.at(t).observe(comet).radec()
print(ra)
print(dec)
