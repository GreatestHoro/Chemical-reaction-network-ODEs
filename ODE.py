import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
from threading import Timer

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

    return dAdt

index = count()
def Concentrations():


    A = con[0]
    B = con[1]
    C = con[2]
    D = con[3]
    E = con[4]


    return [A, B, C, D, E]


def euler() :
    eq1 = ODES(con, 1)
    print(eq1)
    y0 = con[0]
    h = 0.1
    n = 10
    i = 0 
    yn = 0
    
    while i < n : 
        yn = y0 + h * eq1
        y0 = yn 
        i = i + 1

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