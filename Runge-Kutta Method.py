import math
import matplotlib.pyplot as plt

#derivative we're fiding
def fun(t,x):
    return math.atan(x*t)

dt = 0.01

#initial conditions
t = 0
x = 1

#arrays used for plotting
ts = [t]
xs = [x]

while t < 10:
    k1 = fun(t, x)
    k2 = fun(t+dt/2, x+dt*k1/2)
    k3 = fun(t+dt/2, x+dt*k2/2)
    k4 = fun(t+dt,   x+dt*k3)

    xs.append(x)
    ts.append(t)

    x = x + dt/6*(k1+2*k2+2*k3+k4)
    t = t + dt

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(ts, xs)
plt.show()
