import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
from threading import Timer
import warnings

con = [1,1,1,1,1]
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


    A = con[0]
    B = con[1]
    C = con[2]
    D = con[3]
    E = con[4]


    return [A, B, C, D, E]


def euler() :
        ft = 10     #final t
        h = 0.00125    #step size
        t = np.arange(0,ft + 0.5,h)

        print ("T value")
        print (t)
        n = len(t)

        cA = np.ones(n)
        cB = np.ones(n)
        cC = np.ones(n)
        cD = np.ones(n)
        cE = np.ones(n)

        for i in range(0,n):
            cA[i] = 100
            cB[i] = 90
            cC[i] = 80
            cD[i] = 70
            cE[i] = 60

        print(cA,cB,cC,cD,cE)
        
        #Rates
        k1 = 1  #Alpha
        k2 = 1  #Beta
        k3 = 1  #Gamme
        k4 = 1  #Epsillion
        k5 = 1  #Delta
        k6 = 1  #Zeta
        k7 = 1  #Theta
        
        for i in range(1,n):
            r1 = k1 * cA[i-1]
            r2 = k2 * cB[i-1]
            r3 = k3 * cA[i-1] * cC[i-1]
            r4 = k4 * cD[i-1]
            r5 = k5 * cB[i-1] * cE[i-1]
            r6 = k6 * cB[i-1] * cE[i-1]
            r7 = k7 * cE[i-1]

            cA[i] = (-r1 + r2 - r3 + r6) * h + cA[i-1]
            cB[i] = (r1 - r2 + r4 - r5 - r6) * h + cB[i-1]
            cC[i] = (-r3 + r6 + r7) * h + cC[i-1]
            cE[i] = (r3 - r4 + r5 ) * h + cD[i-1]
            cD[i] = (r4 - r7 - r6) * h + cE[i-1]
            
        plt.cla()
        plt.plot(t, cA)
        plt.plot(t, cB)
        plt.plot(t, cC)
        plt.plot(t, cD)
        plt.plot(t, cE)

        plt.xlabel('Time (s)')
        plt.ylabel('Concentration')
        plt.legend(['cA','cB','cC','cD','cE'])
        plt.show()



euler()

# def animate(i):
#     t = np.linspace(0, 10, 100)
#     c0 = con

#     c = odeint(ODES, c0 ,t)

#     plt.cla()
#     plt.plot(t,c[:,0])
#     plt.plot(t,c[:,1])
#     plt.plot(t,c[:,2])
#     plt.plot(t,c[:,3])
#     plt.plot(t,c[:,4])

#     plt.xlabel('Time (s)')
#     plt.ylabel('Concentration')
#     plt.legend(['cA','cB','cC','cD','cE'])
    

# ani = FuncAnimation(plt.gcf(), animate, interval = 1000)

# plt.tight_layout()
# # plt.show()