import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

sigma = 10
r = 27
b = 8 / 3

def Lorenz(y, t):
    y1 = y[0]
    y2 = y[1]
    y3 = y[2]
    global sigma
    global r
    global b
    return [sigma * (y2 - y1), - y2 + y1 * (r - y3), - b * y3 + y1 *y2]

y0 = [-8.48, -8.48, 27]
t = np.linspace(0., 200, 20000)

dydt = odeint (Lorenz, y0, t)
y1 = dydt[:,0]
y2 = dydt[:,1]
y3 = dydt[:,2]
V = y1*y2*y3

plt.figure()

plt.plot(y1, y2)
plt.show()

plt.plot(y1, y3)
plt.show()

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(y1, y2, y3)
plt.show()
