import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(10,100,1000)
y=np.exp(-x*np.sin(x))
plt.ylabel("Это ось Y")
plt.xlabel("Это ось X")
plt.grid()
plt.minorticks_on()
plt.plot(x,y)
plt.show()