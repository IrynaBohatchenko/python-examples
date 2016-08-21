import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

a = 0.02
b = -0.1
c = -55
d = 6
k1 = 0.04
k2 = 5
k3 = 140
vThr = 30

v0 = -70.
u0 = -20.

def Neuron (y, t):
    global a
    global b
    global c
    global d
    global k1
    global k2
    global k3
    I = 0
    y1 = y[0]
    y2 = y[1]
    v = k1 * y1 * y1 + k2 * y1 + k3 -y2 + I
    u = a * (b * y1 - y2)
    return [v, u]

y0 = [v0, u0]
t = np.linspace(0., 500, 100000)

dydt = odeint(Neuron, y0, t)
v = dydt[:, 0]
u = dydt[:, 1]
print (v)
print (u)

plt.plot(t, v)
plt.show()

plt.plot(t, u)
plt.show()
