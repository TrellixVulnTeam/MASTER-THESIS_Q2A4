# Small body Database (SBDB)

from astropy import time
from matplotlib import pyplot as plt
from poliastro.bodies import Sun, Earth, Moon
from poliastro.bodies import Earth
from poliastro.frames import Planes
from poliastro.plotting import StaticOrbitPlotter
from poliastro.twobody.orbit import Orbit

plt.style.use('seaborn-whitegrid')
ivar = Orbit.from_sbdb("Ivar")
uy4 = Orbit.from_sbdb("194268")
SG276 = Orbit.from_sbdb("194126")
rp8 = Orbit.from_sbdb("455432")
ql7 = Orbit.from_sbdb("18172")
tu3 = Orbit.from_sbdb("66146")

frame = StaticOrbitPlotter(plane=Planes.EARTH_ECLIPTIC)
frame.plot(ivar, label="Ivar 1627")
frame.plot(uy4, label="2001UY4")
frame.plot(SG276, label="2001SG276")
frame.plot(rp8, label="2003RP8")
frame.plot(ql7, label="2000QL7")
frame.plot(tu3, label="1998TU3")

plt.savefig('NEA orbits.svg', dpi=1000)


plt.show()


