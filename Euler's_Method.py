import matplotlib.pyplot as plt

def fun(x,y):
    #dy/dx = f(x,y)
    return x*y

dx = 0.01

x = [1]
y = [1]

plt.ion()
#plt.rcParams['toolbar'] = 'None'

fig = plt.figure()
ax = fig.add_subplot(111)

line, = ax.plot(x,y)

for i in range(100):
    y.append(y[-1] + dx*fun(x[-1],y[-1]))
    x.append(x[-1] + dx)
    line.set_data(x,y)
    plt.draw()
    plt.pause(0.1)

plt.ioff()
plt.show()