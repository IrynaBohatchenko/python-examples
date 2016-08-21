import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D
from numpy import linalg as lg
from math import log

sigma = 10
r = 28
b = 8 / 3
m = 25000
dt = 0.01

def Lorenz(y, t):
    y1 = y[0]
    y2 = y[1]
    y3 = y[2]
    global sigma
    global r
    global b
    return [sigma * (y2 - y1), - y2 + y1 * (r - y3), - b * y3 + y1 *y2]

def Correlation (y, T):
    R = 0.0
    global dt
    global m
    for k in range (1, 250):
        R += y[k * dt] * y[k * dt + T]
    R = R / (m * dt)
    return R

def H_S (x):
    return 0.5 * (np.sign(x) + 1)

def Count_C (r, y):
    global dt
    global N
    print (r)
    C = 0
    counter = 0
    for j in range (1, N):
        for k in range (1, N):
            if k == j:
                continue
            y1 = y[:, j * dt] - y[:,k * dt]
            C += H_S(r - lg.norm(y1))
    C = C / (N * N)
    return C

def Count_C_Dep (y1, y2, y3):
    f1 = open('my\\one_meas9_10.txt', 'w')
    f2 = open('my\\two_meas.txt', 'w')
    f3 = open('my\\three_meas1_4.txt', 'w')
    for r in range (1, 5):
        f1.write('r = ' + str(r) + '\n C = ' + str (Count_C(r, np.array([y1]))) + '\n')
        f2.write('r = ' + str(r) + 'C = ' + str(Count_C(r, np.array([y1, y2]))) + '\n')
        f3.write('r = ' + str(r) + ' C = ' + str(Count_C(r, np.array([y1, y2, y2]))) + '\n')
    f1.close()
    f2.close()
    f3.close()

y0 = [1, 1, 1]
t = np.linspace(32., m * dt + 32, 25000)

dydt = odeint (Lorenz, y0, t)
y1 = dydt[:,0]
y2 = dydt[:,1]
y3 = dydt[:,2]

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(y1, y2, y3)
plt.show()
