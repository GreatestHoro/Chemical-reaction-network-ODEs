import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
from threading import Timer


#Equation 4.11, ODE.
#Returns a system of ODEs, as a list
def ODES(C, t):
    #Concentrations
    cA = C[0]
    cB = C[1]
    cC = C[2]
    cD = C[3]
    cE = C[4]

    #Rates
    k1 = 1  #Alpha
    k2 = 1  #Beta
    k3 = 1  #Gamme
    k4 = 1  #Epsillion
    k5 = 1  #Delta
    k6 = 1  #Zeta
    k7 = 1  #Theta

    #Reactions
    r1 = k1 * cA
    r2 = k2 * cB
    r3 = k3 * cA * cC
    r4 = k4 * cD
    r5 = k5 * cB * cE
    r6 = k6 * cB * cE
    r7 = k7 * cE

    #ODES
    dAdt = -r1 + r2 - r3 + r6
    dBdt = r1 - r2 + r4 - r5 - r6
    dCdt = -r3 + r6 + r7
    dDdt = r3 - r4 + r5 
    dEdt = r4 - r7 - r6

    return [dAdt, dBdt, dCdt, dDdt, dEdt]

index = count()
def Concentrations(): 
    A = 1
    B = 100
    C = 1
    D = 1
    E = 1

    # while True :
    #     if A < B : 
    #         A = A + 1
    #     elif A == B : 
    #         print ("equlibrium")
    #         False
    #     else :
    #         print("Still not netrual")


    return [A, B, C, D, E]


def animate(i):

    t = np.linspace(0, 1 + next(index), 100)
    c0 = Concentrations()
    c = odeint(ODES, c0,t)

    print(c0)
    plt.cla()
    plt.plot(t,c[:,0])
    plt.plot(t,c[:,1])
    plt.plot(t,c[:,2])
    plt.plot(t,c[:,3])
    plt.plot(t,c[:,4])

    plt.xlabel('Time (s)')
    plt.ylabel('Concentration')
    plt.legend(['cA','cB','cC','cD','cE'])
    

ani = FuncAnimation(plt.gcf(), animate, interval = 1000)

plt.tight_layout()
plt.show()