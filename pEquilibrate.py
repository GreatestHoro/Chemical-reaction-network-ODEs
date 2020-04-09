import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
from threading import Timer
import warnings
import protocols

def equilibrate(sample):
    ani = FuncAnimation(plt.gcf(), sample.Animate, interval=1000)
    plt.show()