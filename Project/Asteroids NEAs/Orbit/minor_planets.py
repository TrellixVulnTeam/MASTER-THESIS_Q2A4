# mpc_make_excerpt.py

"""Search the MPCORB file for minor planets, given their packed designations."""

import argparse
import re
import sys
import zlib

from skyfield.constants import GM_SUN_Pitjeva_2005_km3_s2 as GM_SUN
from skyfield.api import load
from skyfield.data import mpc

# def main(argv):
#    parser = argparse.ArgumentParser(description='Gzep nea_extended.dat.gz')
#    parser.add_argument('designations', nargs='+', help='packed designations'
#                                                        ' of the minor planets whose orbits you need')
#    args = parser.parse_args(argv)

#    designations = [re.escape(d.encode('ascii')) for d in args.designations]
#    pattern = rb'^((?:%s) .*\n)' % rb'|'.join(designations)
#    r = re.compile(pattern, re.M)

#    data = load.open(mpc.MPCORB_URL).read()
#    data = zlib.decompress(data, wbits=zlib.MAX_WBITS | 16)
#    lines = r.findall(data)

#    sys.stdout.buffer.write(b''.join(lines))


# if __name__ == '__main__':
#    main(sys.argv[1:])

with load.open('nea_extended.dat') as f:
    minor_planets = mpc.load_mpcorb_dataframe(f)

file = open('NEA.txt', 'wt')
# sys.stdout = file
print(minor_planets.shape[0], 'minor planets loaded\n')

# Filtering the orbits dataframe to avoid triggering
# an `EphemerisRangeError` on ill-defined orbits.

bad_orbits = minor_planets.semimajor_axis_au.isnull()
minor_planets = minor_planets[~bad_orbits]

# Index by designation for fast lookup.
minor_planets = minor_planets.set_index('designation', drop=False)

# Sample lookups.
row = minor_planets.loc['(1627) Ivar']
row = minor_planets.loc['(18172) 2000 QL7']
row = minor_planets.loc['(66146) 1998 TU3']
row = minor_planets.loc['(194126) 2001 SG276']
row = minor_planets.loc['(194268) 2001 UY4']
row = minor_planets.loc['(455432) 2003 RP8']

ts = load.timescale()
eph = load('de421.bsp')
sun, earth = eph['sun'], eph['earth']

t = ts.utc(2020, 5, 31)
# IVAR
ivar = sun + mpc.mpcorb_orbit(row, ts, GM_SUN)
ra, dec, distance = earth.at(t).observe(ivar).radec()
print('(1627) IVAR')
print('RA', ra)
print('DEC', dec)

# (18172) 2000 QL7
ql = sun + mpc.mpcorb_orbit(row, ts, GM_SUN)
ra, dec, distance = earth.at(t).observe(ql).radec()
print('\n(18172) 2000 QL7')
print('RA', ra)
print('DEC', dec)

# (66146) 1998 TU3
tu = sun + mpc.mpcorb_orbit(row, ts, GM_SUN)
ra, dec, distance = earth.at(t).observe(tu).radec()
print('\n(66146) 1998 TU3')
print('RA', ra)
print('DEC', dec)

# (194126) 2001 SG276
sg = sun + mpc.mpcorb_orbit(row, ts, GM_SUN)
ra, dec, distance = earth.at(t).observe(sg).radec()
print('\n(194126) 2001 SG276')
print('RA', ra)
print('DEC', dec)

# (194268) 2001 UY4
uy = sun + mpc.mpcorb_orbit(row, ts, GM_SUN)
ra, dec, distance = earth.at(t).observe(uy).radec()
print('\n(194268) 2001 UY4')
print('RA', ra)
print('DEC', dec)

# (194268) 2001 UY4
rp = sun + mpc.mpcorb_orbit(row, ts, GM_SUN)
ra, dec, distance = earth.at(t).observe(rp).radec()
print('\n(455432) 2003 RP8 ')
print('RA', ra)
print('DEC', dec)
