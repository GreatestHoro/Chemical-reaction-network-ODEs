import matplotlib.pyplot as plt
import numpy as np
from ODE import euler

point_list = euler()
temp = np.asarray(point_list, dtype = np.float32)
print(temp)
ft = 10        #final t
h = 0.00125    #step size
t = np.arange(0,5)
# You probably won't need this if you're embedding things in a tkinter plot...
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(t, temp[:,0])
line2, = ax.plot(t, temp[:,1])
line1, = ax.plot(t, temp[:,2])
line2, = ax.plot(t, temp[:,3])
line1, = ax.plot(t, temp[:,4])
print(temp)
for i in range(1,10):
    line1.set_ydata(t + i)
    line2.set_ydata(t + i)
    fig.canvas.draw()
    fig.canvas.flush_events()

    print (temp[0][i])



