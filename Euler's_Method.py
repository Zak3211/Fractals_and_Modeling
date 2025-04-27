import matplotlib.pyplot as plt
import math

def fun(x,y):
    #dy/dx = f(x,y)
    return x/y

dx = 0.1

x = [1]
y = [1]

plt.ion()
#plt.rcParams['toolbar'] = 'None'

fig = plt.figure()
ax = fig.add_subplot(1,1)

num_steps = 10000

line, = ax.plot(x,y)
xmin = x[0]
ymin = y[0]

xmax = x[0] + num_steps*dx
ymax = y[0]

ax.set_xlim(xmin-10, xmax+ 10)
for i in range(100):
    ax.set_ylim(ymin-10, ymax + 10)

    ymax = max(ymax, y[-1])
    ymin = min(ymin, y[-1])

    y.append(y[-1] + dx*fun(x[-1],y[-1]))
    x.append(x[-1] + dx)
    line.set_data(x,y)
    plt.draw()
    plt.pause(0.1)

plt.ioff()
plt.show()