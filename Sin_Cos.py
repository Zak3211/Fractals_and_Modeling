import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import matplotlib.gridspec as gridspec

plt.ion()
plt.rcParams['toolbar'] = 'None'

fig = plt.figure(figsize=plt.figaspect(1.))
fig.canvas.manager.set_window_title("Sin and Cos")
gs = gridspec.GridSpec(2, 2, figure=fig)

x, y, z = [0],[math.sin(0)], [math.cos(0)]
dt = 0.1

#Code for first Graph (Sin and Cosine)
ax1 = fig.add_subplot(gs[0:2, 0:1], projection = '3d')

ax1.set_xlim(0, 30) 
ax1.set_ylim(-2, 2)  
ax1.set_zlim(-2, 2) 


line1, = ax1.plot(x, y, z, color = 'Blue')

#Code for second Graph (Sine)
ax2 = fig.add_subplot(222)
line2, = ax2.plot(x,y, color = 'red')

ax2.set_xlim(0, 30) 
ax2.set_ylim(-2, 2)  

#Code for third graph (Cosine graph)
ax3 = fig.add_subplot(224)
line3, = ax3.plot(x,z, color = 'red')

ax3.set_xlim(0, 30) 
ax3.set_ylim(-2, 2)  

#Main loop
while True:
    x.append(x[-1] + dt)
    y.append(math.sin(x[-1]))
    z.append(math.cos(x[-1]))

    line1.set_data(x, y)
    line1.set_3d_properties(z)

    line2.set_data(x,y)

    line3.set_data(x,z)

    #reinitialize the arrays to create loop
    if x[-1] == 30:
        x, y, z = [0],[math.sin(0)], [math.cos(0)]
        plt.draw()

    plt.draw()
    plt.pause(0.01)

plt.ioff()
plt.show()