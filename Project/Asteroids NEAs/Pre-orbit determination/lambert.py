from lamberthub import gooding1990
# from lamberthub import gauss1809
# Import NumPy for declaring position vectors
import numpy as np

# Initial conditions for the problem
mu_sun = 5.930083518957107e-06  # [AU ** 3 / s ** 2]
r1 = np.array([-1.035551254166514, -9.773185230470425e-1, 2.122296155587400e-1])  # [AU]
r2 = np.array([-1.020836945470817, -9.847652361333888e-1, 2.113906469630352e-1])  # [AU]
tof = 90000  # [seconds]

R1 = np.linalg.norm(r1)
R2 = np.linalg.norm(r2)
# print(R1)
print(R2)
# au = 149597870.7
# mu = 1.32712440018e11
# print(mu/(au**2))
# Solving the problem
v1, v2 = gooding1990(mu_sun, r1, r2, tof)
# v1, v2 = gauss1809(mu_sun, r1, r2, tof)
# Let us print the results
print(f"Initial velocity: {v1} [AU/s]\nFinal velocity  : {v2} [AU/s]")
V1 = np.linalg.norm(v1)
V2 = np.linalg.norm(v2)
# print(V1)
print(V2)
# orbital elements
# angular momentum
h = R2 * V2
print(h, '[AU^2/s]')

# eccentricity
e = ((V2 * h) / mu_sun) - (R2 / abs(R2))
print(e)
# ecc = (-0.37882205 * -0.89028507 * -0.99963168) ** (1 / 3)
# print(f'Eccentricity: {ecc}')
