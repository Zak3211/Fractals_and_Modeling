import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math

plt.ion()
plt.rcParams['toolbar'] = 'None'

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

ax.set_xlim(0, 30) 
ax.set_ylim(-2, 2)  
ax.set_zlim(-2, 2) 

"""
ax.set_facecolor('black')
fig.patch.set_facecolor('black')
ax.grid(False)
ax.set_axis_off()


ax.xaxis.pane.set_facecolor('black')
ax.yaxis.pane.set_facecolor('black')
ax.zaxis.pane.set_facecolor('black')
"""
fig.canvas.manager.set_window_title("Sin and Cos")

dt = 0.1

x, y, z = [],[], []

x.append(0)
y.append(math.sin(0))
z.append(math.cos(0))

line, = ax.plot(x, y, z, color = 'Blue')

while x[-1] < 30:
    x.append(x[-1] + dt)
    y.append(math.sin(x[-1]))
    z.append(math.cos(x[-1]))
    
    line.set_data(x, y)
    line.set_3d_properties(z)
    plt.draw()
    plt.pause(0.01)

plt.ioff()
plt.show()