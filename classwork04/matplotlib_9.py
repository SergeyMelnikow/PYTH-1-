import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(50,100,1000)
y=x*np.sin(x)**2
plt.yscale('log')
plt.ylabel("Этo ocь  Y(lg(y))")
plt.xlabel("Это ось X")
plt.grid()
plt.minorticks_on()
plt.plot(x,y,label="синяя линия:y=x*sin(x)^2")
plt.title("y=x*np.sin(x)**2")
plt.legend()
plt.show()
