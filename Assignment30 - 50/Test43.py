import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,4*np.pi,0.1)   # start,stop,step
z = np.cos(x)
plt.plot(x,z)
plt.show()