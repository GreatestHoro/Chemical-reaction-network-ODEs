import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
from threading import Timer
import warnings
import protocols

index = count()
stepList = []
iter = [100, 20, 100, 100, 100]
name = ['A', 'B', 'C', 'D', 'E']

sample_A = {"A":[100],
            "B":[90],
            "C":[80],
            "D":[70],
            "E":[60]
}

ft = 100            #final t
h = 0.00125         #step size
t = np.arange(0,ft + 0.5,1)
n = len(t)

def oneEuler(sample) :
    k1 = 1  #Alpha
    k2 = 1  #Beta
    k3 = 1  #Gamme
    k4 = 1  #Epsillion
    k5 = 1  #Delta
    k6 = 1  #Zeta
    k7 = 1  #Theta

    r1 = k1 * sample.get("A")[-1]
    r2 = k2 * sample.get("B")[-1]
    r3 = k3 * sample.get("A")[-1] * sample.get("C")[-1]
    r4 = k4 * sample.get("D")[-1]
    r5 = k5 * sample.get("B")[-1] * sample.get("E")[-1]
    r6 = k6 * sample.get("B")[-1] * sample.get("E")[-1]
    r7 = k7 * sample.get("E")[-1]

    sample["A"].append((-r1 + r2 - r3 + r6) * h + sample.get("A")[-1])
    sample["B"].append((r1 - r2 + r4 - r5 - r6) * h + sample.get("B")[-1])
    sample["C"].append((-r3 + r6 + r7) * h + sample.get("C")[-1])
    sample["D"].append((r3 - r4 + r5 ) * h + sample.get("D")[-1])
    sample["E"].append((r4 - r7 - r6) * h + sample.get("E")[-1])

    return sample

def applyTitration(sample, i):
    cSample = sample.copy()

    if i % 2 == 0:
        cSample["A"][-1] = cSample.get("A")[-1] + 1

    if i % 5 == 0:
        if cSample.get("A")[-1] - 100 <= 0 :
            cSample.get("A")[-1] = 0 
        else :
            cSample["A"][-1] = cSample.get("A")[-1] - 100

    return cSample
     

def ani_sample_A(i) :
    global sample_A

    plt.cla()
    ax1 = plt.subplot(212)
    ax1.grid(True, linestyle='-.')
    ax2 = plt.subplot(211)

    stepList.append(next(index))
    for key, value in sample_A.items():
        ax1.plot(stepList, value, label=key)
        ax2.plot(stepList, value, label=key)
        plt.legend()
    
    sample_A = oneEuler(sample_A)
    sample_A = applyTitration(sample_A, i+1)

ani = FuncAnimation(plt.gcf(), ani_sample_A, interval=1000)


sample_B = {}
sample_C = {}
sample_D = {}

sample_A, [sample_B, sample_C] = protocols.split(sample_A, [sample_B, sample_C], [0.1, 0.1])

sample_D = protocols.mix([sample_B, sample_C])

plt.show()