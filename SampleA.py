import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
from threading import Timer
import warnings
import protocols
from interface import implements, Interface

from ISample import ISample

class SampleA(implements(ISample)):

    stepList = []
    index = count()
    sample_A = {"A":[100],
                "B":[90],
                "C":[80],
                "D":[70],
                "E":[60]
    }

    iter = [100, 20, 100, 100, 100]
    
    ft = 100            #final t
    h = 0.00125         #step size
    t = np.arange(0,ft + 0.5,1)
    n = len(t)

    def Euler(self) :
        k1 = 1  #Alpha
        k2 = 1  #Beta
        k3 = 1  #Gamme
        k4 = 1  #Epsillion
        k5 = 1  #Delta
        k6 = 1  #Zeta
        k7 = 1  #Theta

        r1 = k1 * self.sample_A.get("A")[-1]
        r2 = k2 * self.sample_A.get("B")[-1]
        r3 = k3 * self.sample_A.get("A")[-1] * self.sample_A.get("C")[-1]
        r4 = k4 * self.sample_A.get("D")[-1]
        r5 = k5 * self.sample_A.get("B")[-1] * self.sample_A.get("E")[-1]
        r6 = k6 * self.sample_A.get("B")[-1] * self.sample_A.get("E")[-1]
        r7 = k7 * self.sample_A.get("E")[-1]

        
        self.sample_A["A"].append((-r1 + r2 - r3 + r6) * self.h + self.sample_A.get("A")[-1])
        self.sample_A["B"].append((r1 - r2 + r4 - r5 - r6) * self.h + self.sample_A.get("B")[-1])
        self.sample_A["C"].append((-r3 + r6 + r7) * self.h + self.sample_A.get("C")[-1])
        self.sample_A["D"].append((r3 - r4 + r5 ) * self.h + self.sample_A.get("D")[-1])
        self.sample_A["E"].append((r4 - r7 - r6) * self.h + self.sample_A.get("E")[-1])

    def ApplyTitration(self, i):
        if i % 2 == 0:
            self.sample_A["A"][-1] = self.sample_A.get("A")[-1] + 1

        if i % 5 == 0:
            if self.sample_A.get("A")[-1] - 100 <= 0 :
                self.sample_A.get("A")[-1] = 0 
            else :
                self.sample_A["A"][-1] = self.sample_A.get("A")[-1] - 100

    @staticmethod
    def Animate(i) :
        plt.cla()
        ax1 = plt.subplot(212)
        ax1.grid(True, linestyle='-.')
        ax2 = plt.subplot(211)

        SampleA.stepList.append(next(SampleA.index))

        for key, value in SampleA.sample_A.items():
            ax1.plot(SampleA.stepList, value, label=key)
            ax2.plot(SampleA.stepList, value, label=key)
            plt.legend()
        
        SampleA.Euler(SampleA)
        SampleA.ApplyTitration(SampleA, i+1)