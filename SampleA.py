import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
from threading import Timer
import warnings
import protocols

class SampleQ():
    sample = {
        "A":[100],
        "B":[90],
        "C":[80],
        "D":[70],
        "E":[60]
    }

    stepList = []
    index = count()
    ft = 100
    t = np.arange(0,ft + 0.5,1)
    n = len(t)
    h = 0.0025
    def Euler(self) :
        r1=1*self.sample.get("A")[-1]
        r2=1*self.sample.get("B")[-1]
        r3=1*self.sample.get("A")[-1]*self.sample.get("C")[-1]
        r4=1*self.sample.get("D")[-1]
        r5=1*self.sample.get("B")[-1]*self.sample.get("E")[-1]
        r6=1*self.sample.get("B")[-1]*self.sample.get("E")[-1]
        r7=1*self.sample.get("E")[-1]
        self.sample["A"].append((-r1+r2-r3+r6)*self.h+self.sample.get("A")[-1])
        self.sample["B"].append((r1-r2+r4-r5-r6)*self.h+self.sample.get("B")[-1])
        self.sample["C"].append((-r3+r6+r7)*self.h+self.sample.get("C")[-1])
        self.sample["D"].append((r3-r4+r5)*self.h+self.sample.get("D")[-1])
        self.sample["E"].append((r4-r5-r6-r7)*self.h+self.sample.get("E")[-1])
    def ApplyTitration(self,i):
        if i % 20 == 0 :
            self.sample["A"][-1] = self.sample.get("A")[-1]+1

    @staticmethod
    def Animate(i) :
        plt.cla()

        SampleQ.stepList.append(next(SampleQ.index))

        for key, value in SampleQ.sample.items():
            plt.plot(SampleQ.stepList, value, label=key)
            plt.legend()

        SampleQ.Euler(SampleQ)
        SampleQ.ApplyTitration(SampleQ, i+1)