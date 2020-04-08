import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
from threading import Timer
import warnings


index = count()
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
# def Concentrations():

#     global cA, cB, cC, cD, cE, con
#     for i in range(1,n):
#         cA[i] = con[0]
#         cB[i] = con[1]
#         cC[i] = con[2]
#         cD[i] = con[3]
#         cE[i] = con[4]
# Concentrations()
def euler() :
        con = [100,90,80,70,60]
        ft = 10        #final t
        h = 0.00125    #step size
        t = np.arange(0,ft + 0.5,1)
        n = len(t)

        cA = np.ones(n)
        cB = np.ones(n)
        cC = np.ones(n)
        cD = np.ones(n)
        cE = np.ones(n) 

        cA[0] = con[0]
        cB[0] = con[1]
        cC[0] = con[2]
        cD[0] = con[3]
        cE[0] = con[4]

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

        return [cA,cB,cC,cD,cE]
        # j += 1

   
euler()
# ani = FuncAnimation(plt.gcf(), euler, interval = 1000)

