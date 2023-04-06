import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
f = pd.read_csv("TIME(N).csv")

x = f["kristal_size"]**2
y = np.array(f["Microseconds"])
err = np.array(x)
plt.scatter(x,y,s=5,c='r',label = 'Время движения в зависимости от размера кристалла')


k=(((y*x).mean())/((x*x).mean()))
print(k,"\n")
x=np.linspace(0,1.2*x[len(x)-1],1000)
y=np.array([k*i for i in x])
plt.plot(x,y,'r',linestyle = '--',label = 'по МНК')

plt.xlabel("Size")
plt.ylabel("Microseconds")
plt.grid()
plt.minorticks_on()
plt.legend()
plt.show()