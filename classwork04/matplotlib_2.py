import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-1,1,100)
y=np.sin(x)*x**(-2)
plt.plot(x,y)
plt.ylabel("Это ось Y")
plt.xlabel("Это ось X")
plt.grid()
plt.show()