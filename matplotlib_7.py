import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(50,100,1000)
y=x*np.sin(x)**2
plt.ylabel("Этo ocь  Y")
plt.xlabel("Это ось X")
plt.grid()
plt.minorticks_on()
plt.plot(x,y)
plt.show()