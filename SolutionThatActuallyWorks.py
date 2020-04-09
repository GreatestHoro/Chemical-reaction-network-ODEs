import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
from threading import Timer
import warnings


amount = 5

index = count()

caMa = [[] for i in range(amount)]
stepList = []
iter = [100, 20, 100, 100, 100]
name = ['A', 'B', 'C', 'D', 'E']
style = ['g-','ro-','b:','y-.', 'b--']
pre_val = [100,90,80,70,60]

ft = 100            #final t
h = 0.00125         #step size
t = np.arange(0,ft + 0.5,1)
n = len(t)

def oneEuler(val) :
    old = val.copy()
    
    k1 = 1  #Alpha
    k2 = 1  #Beta
    k3 = 1  #Gamme
    k4 = 1  #Epsillion
    k5 = 1  #Delta
    k6 = 1  #Zeta
    k7 = 1  #Theta

    r1 = k1 * val[0]
    r2 = k2 * val[1]
    r3 = k3 * val[0] * val[2]
    r4 = k4 * val[3]
    r5 = k5 * val[1] * val[4]
    r6 = k6 * val[1] * val[4]
    r7 = k7 * val[4]

    val[0] = (-r1 + r2 - r3 + r6) * h + old[0]
    val[1] = (r1 - r2 + r4 - r5 - r6) * h + old[1]
    val[2] = (-r3 + r6 + r7) * h + old[2]
    val[3] = (r3 - r4 + r5 ) * h + old[3]
    val[4] = (r4 - r7 - r6) * h + old[4]

    return val


def animate(i) :
    global pre_val

    pre_val = oneEuler(pre_val)
    plt.cla()
    
    ax1 = plt.subplot(212)
    ax1.grid(True, linestyle='-.')
    ax2 = plt.subplot(211)
    stepList.append(next(index))
    for j in range(0, amount):
        if i <= iter[j] :
            caMa[j].append(pre_val[j])
        ax1.plot(stepList, caMa[j], style[j] ,label=name[j])
        ax2.plot(stepList, caMa[j], style[j] ,label=name[j])
        plt.legend()

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.show()