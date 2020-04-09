import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
from threading import Timer
import warnings
import random


index = count()

x_vals1 = []
x_vals2 = []
x_vals3 = []
x_vals4 = []
x_vals5 = []
y_vals = []
k = 0
j = 1
h = 0.00125

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
con = [100,90,80,70,60]
def euler() :
        cAh = 0
        global con, h
        ft = 10        #final t
        t = np.arange(0,ft+0.5,h)
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
            cD[i] = (r3 - r4 + r5 ) * h + cD[i-1]
            cE[i] = (r4 - r7 - r6) * h + cE[i-1]
            
        
        
        return [cA,cB,cC,cD,cE]
        # return h
        # j += 1

def animate(i) :
    global j, k, h
    # j = 0
    # i = 0 + next(index)
    data = euler()
    # t = np.linspace(0,5,j + next(index))

    # plt.plot(t,data[0][i], 'r-')
    # plt.plot(t,data[1][i], 'y-')
    # plt.plot(t,data[2][i], 'b-')
    # plt.plot(t,data[3][i], 'g')
    # plt.plot(t,data[4][i], 'p-')
    x_vals1.append(data[0][0 + k])
    x_vals2.append(data[1][0 + k])
    x_vals3.append(data[2][0 + k])
    x_vals4.append(data[3][0 + k])
    x_vals5.append(data[4][0 + k])
    y_vals.append(j)

    plt.cla()
    plt.plot(y_vals, x_vals1)
    plt.plot(y_vals, x_vals2)
    plt.plot(y_vals, x_vals3)
    plt.plot(y_vals, x_vals4)
    plt.plot(y_vals, x_vals5)


    plt.xlabel('Time (t)')
    plt.ylabel('Concentration (mol/L)')
    plt.title('Species evolution over time')
    plt.legend(['cA', 'cB', 'cC', 'cD', 'cE'])

    x_pltpr = 50
    k += x_pltpr
    j = j + (x_pltpr * h) 

def ode_plot(): 

    c0 = con
    t = np.linspace(1, 10)
    c = odeint(ODES,c0,t, full_output = True)
    print (c[1].get('hu')[0])
    ode_plot = plt.subplot(212)
    ode_plot.plot(t,c[:,0])
    ode_plot.plot(t,c[:,1])
    ode_plot.plot(t,c[:,2])
    ode_plot.plot(t,c[:,3])
    ode_plot.plot(t,c[:,4])
    ode_plot.xlabel('Time (t)')
    ode_plot.ylabel('Concentration (mol/L)')
    ode_plot.title('Species evolution over time')
    ode_plot.legend(['cA', 'cB', 'cC', 'cD', 'cE'])

def euler_plot():
    c0 = con
    t = np.arange(1,10,h)
    c = odeint(ODES,c0,t)

    ode_plot = plt.subplot(212)
    ode_plot.plot(t,c[:,0])
    ode_plot.plot(t,c[:,1])
    ode_plot.plot(t,c[:,2])
    ode_plot.plot(t,c[:,3])
    ode_plot.plot(t,c[:,4])
    plt.xlabel('Time (t)')
    plt.ylabel('Concentration (mol/L)')
    plt.title('Species evolution over time')
    plt.legend(['cA', 'cB', 'cC', 'cD', 'cE'])

    
    data = euler()
    tsize = len(data)
    t2 = np.linspace(1,10,8400)

    euler_plot = plt.subplot(211)
    euler_plot.plot(t2,data[0])
    euler_plot.plot(t2,data[1])
    euler_plot.plot(t2,data[2])
    euler_plot.plot(t2,data[3])
    euler_plot.plot(t2,data[4])


    plt.xlabel('Time (t)')
    plt.ylabel('Concentration (mol/L)')
    plt.title('Species evolution over time')
    plt.legend(['cA', 'cB', 'cC', 'cD', 'cE'])

#euler()

euler_plot()

#ode_plot()
#ani = FuncAnimation(plt.gcf(), animate, interval = 1)

plt.tight_layout()
plt.show()

