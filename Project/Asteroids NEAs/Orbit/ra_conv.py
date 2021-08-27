from astropy.coordinates import SkyCoord
from astropy import units as u
from skyfield.positionlib import Barycentric
from skyfield.api import load
from skyfield.data import mpc
from skyfield.constants import GM_SUN_Pitjeva_2005_km3_s2 as GM_SUN

ts = load.timescale()
t = ts.utc(2019, 8, 13, 7, 00, 00)

with load.open('nea_extended.dat') as f:
    minor_planets = mpc.load_mpcorb_dataframe(f)
# asteroid
file = open('NEA.txt', 'wt')
print(minor_planets.shape[0], 'minor planets loaded\n')
minor_planets = minor_planets.set_index('designation', drop=False)
# row = minor_planets.loc['(1627) Ivar']
# row = minor_planets.loc['(18172) 2000 QL7']
# row = minor_planets.loc['(66146) 1998 TU3']
# row = minor_planets.loc['(194126) 2001 SG276']
# row = minor_planets.loc['(194268) 2001 UY4']
row = minor_planets.loc['(455432) 2003 RP8']

# planet
planets = load('de421.bsp')
earth, sun = planets['earth'], planets['sun']
ivar = sun + mpc.mpcorb_orbit(row, ts, GM_SUN)
# Three positions in a single line of code!
d = earth.at(t).observe(ivar).apparent().distance()
ra, dec, distance = earth.at(t).observe(ivar).radec()


def HMS2deg(ra='', dec=''):
    RA, DEC, rs, ds = '', '', 1, 1
    if dec:
        D, M, S = [float(i) for i in dec.split()]
        if str(D)[0] == '-':
            ds, D = -1, abs(D)
        deg = D + (M / 60) + (S / 3600)
        DEC = '{0}'.format(deg * ds)

    if ra:
        H, M, S = [float(i) for i in ra.split()]
        if str(H)[0] == '-':
            rs, H = -1, abs(H)
        deg = (H * 15) + (M / 4) + (S / 240)
        RA = '{0}'.format(deg * rs)

    if ra and dec:
        return RA, DEC
    else:
        return RA or DEC


# output
print('Ivar is {:.5f} au from Earth'.format(d.au))
print('RA', ra)
print('DEC', dec)
# print('RA and DEC in degrees', HMS2deg(ra='15 08 55.53', dec='+09 58 01.1'))
# x = -2.120154488336096
# y = 7.396656396963416e-01
# z = 4.749276490241693e-01
# barycentric = Barycentric([x, y, z]).at(t)
barycentric = earth.at(t)
astrometric = barycentric.observe(ivar)
apparent = astrometric.apparent()
d = apparent.distance()

print('Ivar x,y,z:', barycentric.position.au, 'au')
print('Ivar relative velocity:', astrometric.velocity.km_per_s, 'km/s')
print('Time of observation:', apparent.t.utc_strftime())
