import matplotlib.pyplot as plt
import numpy as np


def lorenz(xyz, *, s=  10, r = 28,  b = 2.5):
    x,y,z = xyz
    x, y, z = xyz
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return np.array([x_dot, y_dot, z_dot])

dt = 0.01
num_steps = 1000

coordinates = np.empty((num_steps + 1, 3))
coordinates[0] = (0, 1, 1.5)

for i in range(num_steps):
    coordinates[i+1] = coordinates[i] + lorenz(coordinates[i])*dt

ax = plt.figure().add_subplot(projection='3d')

ax.plot(*coordinates.T, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")

plt.show()
