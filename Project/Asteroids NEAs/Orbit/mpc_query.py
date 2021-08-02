from astroquery.mpc import MPC
from pprint import pprint
result = MPC.query_object('asteroid', name='QL7')
pprint(result)

eph = MPC.get_ephemeris('(1627)')
print(eph)
