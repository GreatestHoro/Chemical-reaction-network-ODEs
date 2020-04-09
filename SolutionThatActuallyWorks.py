import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
from threading import Timer
import warnings

index = count()
stepList = []
iter = [100, 20, 100, 100, 100]
name = ['A', 'B', 'C', 'D', 'E']

sDict = {"A":[100],
         "B":[90],
         "C":[80],
         "D":[70],
         "E":[60]
}

ft = 100            #final t
h = 0.00125         #step size
t = np.arange(0,ft + 0.5,1)
n = len(t)

def oneEuler(val) :
    k1 = 1  #Alpha
    k2 = 1  #Beta
    k3 = 1  #Gamme
    k4 = 1  #Epsillion
    k5 = 1  #Delta
    k6 = 1  #Zeta
    k7 = 1  #Theta

    r1 = k1 * val.get("A")[-1]
    r2 = k2 * val.get("B")[-1]
    r3 = k3 * val.get("A")[-1] * val.get("C")[-1]
    r4 = k4 * val.get("D")[-1]
    r5 = k5 * val.get("B")[-1] * val.get("E")[-1]
    r6 = k6 * val.get("B")[-1] * val.get("E")[-1]
    r7 = k7 * val.get("E")[-1]

    val["A"].append((-r1 + r2 - r3 + r6) * h + val.get("A")[-1])
    val["B"].append((r1 - r2 + r4 - r5 - r6) * h + val.get("B")[-1])
    val["C"].append((-r3 + r6 + r7) * h + val.get("C")[-1])
    val["D"].append((r3 - r4 + r5 ) * h + val.get("D")[-1])
    val["E"].append((r4 - r7 - r6) * h + val.get("E")[-1])

    return val

def applyTitration(pre_val, i):
    val = pre_val.copy()

    if i % 2 == 0:
        val["A"][-1] = val.get("A")[-1] + 1

    if i % 5 == 0:
        if val.get("A")[-1] - 100 <= 0 :
            val.get("A")[-1] = 0 
        else :
            val["A"][-1] = val.get("A")[-1] - 100

    return val
     

def animate(i) :
    global sDict

    plt.cla()
    ax1 = plt.subplot(212)
    ax1.grid(True, linestyle='-.')
    ax2 = plt.subplot(211)

    stepList.append(next(index))
    for key, value in sDict.items():
        ax1.plot(stepList, value, label=key)
        ax2.plot(stepList, value, label=key)
        plt.legend()
    
    sDict = oneEuler(sDict)
    sDict = applyTitration(sDict, i+1)

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.show()