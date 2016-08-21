from pylab import *
import numpy

x = []
x.append (0.5)
s = []
N = 10000
sn = []
distrib = []
H_She = 0
H_R1 = 0
H_R2 = 0
H1 = []
H2 = []
H3 = []

def sequence():
    global x
    for n in range (1, N):
        x.append (3.8 * x[n-1] * (1 - x[n-1]))

def binary_sequence():
    global x
    global s
    for n in range (N):
        if x[n] > 0.5:
            s.append(1)
        else:
            s.append(0)

def get_blocks(nu):
    global N
    n = N // nu
    i = 0
    global sn
    global s
    while i < n:
        sTemp = 0
        for j in range (nu - 1):
            sTemp += s[i * nu + j] * 2 ** (j)
        sn.append(sTemp)
        i += 1

def get_distrib(nu):
    global  sn
    global distrib
    global N
    for i in range (2 ** nu):
        t = 0
        for j in range (len(sn)):
            if sn[j] == i:
                t += 1
        distrib.append(t / float (N // nu))

def count_Shenon():
    global H_She
    H_She = 0
    for i in range (len(distrib)):
        if distrib[i] <> 0:
            H_She += distrib[i] * log (distrib[i])
    H_She = - H_She
    return H_She

def count_Renyi():
    global H_R1
    global H_R2
    H_R1 = 0
    H_R2 = 0
    for i in range (len(distrib)):
        H_R1 += distrib[i] ** 2
        H_R2 += distrib[i] ** 3
    H_R1 = - log (H_R1)
    H_R2 = - 0.5 * log (H_R2)
    return H_R1, H_R2

sequence()
show ()
binary_sequence()

for nu in range (2,11):
    get_blocks(nu)
    get_distrib(nu)
    count_Shenon()
    H1.append(count_Shenon())
    count_Renyi()
    H2.append(count_Renyi()[0])
    H3.append(count_Renyi()[1])
    sn = []
    distrib = []

print ("Shenon")
print (H1)
print ("Renyi1")
print (H2)
print ("Renyi2")
print (H3)

print (H1[5] - H1[4])
print (H2[8] - H2[7])
print (H3[8] - H3[7])

niu = [2, 3, 4, 5, 6, 7, 8, 9, 10]
plot (niu, H1, niu, H2, niu, H3)
show ()
