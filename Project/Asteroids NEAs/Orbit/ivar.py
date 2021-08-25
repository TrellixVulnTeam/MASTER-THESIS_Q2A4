from matplotlib import pyplot as plt
from poliastro.bodies import Earth, Sun
from poliastro.constants import J2000
from poliastro.examples import churi, iss, molniya
from poliastro.plotting import OrbitPlotter3D
from poliastro.twobody import Orbit
from astropy.time import Time
from poliastro.ephem import Ephem
from poliastro.util import time_range
import numpy as np

eros = Orbit.from_sbdb("eros")

date_launch = Time("2011-11-26 15:02", scale="utc").tdb
date_arrival = Time("2012-08-06 05:17", scale="utc").tdb

earth = Ephem.from_body(
    Earth, time_range(date_launch, end=date_arrival, periods=50)
)
frame = OrbitPlotter3D()
frame.set_attractor(Sun)

frame.plot_body_orbit(Earth, J2000, label=Earth)
frame.plot_ephem(earth, label=Earth)
frame = OrbitPlotter3D()

frame.plot(eros, label="eros")
frame.plot_trajectory(earth.sample(), label=Earth)
plt.show()


