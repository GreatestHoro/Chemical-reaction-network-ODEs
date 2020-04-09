import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
from threading import Timer
import warnings
import protocols
from SampleA import SampleA

sampleAObject = SampleA

sample_A = sampleAObject.sample_A
sample_B = {}
sample_C = {}
sample_D = {}

protocols.equlibrate(sampleAObject)

protocols.split(sample_A, [sample_B, sample_C, sample_D], [0.1, 0.1, 0.1])

sample_B = protocols.mix([sample_A, sample_C])

protocols.disposePercent(sample_B, 0.5)

protocols.dispose(sample_B)