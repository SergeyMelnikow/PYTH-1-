import numpy as np
from matplotlib import pyplot as plt
import math as m
import pandas as pd



f = pd.read_csv("TIME(N).csv")

x = (f['Number']/400)
y = np.array(f["Microseconds"])
err = np.array(x)
plt.scatter(x,y,s=5,c='r',label = 'Время движения в зависимости от доли, занимаемой дислокациями')

plt.xlabel("Part")
plt.ylabel("Microseconds")
plt.grid()
plt.minorticks_on()
plt.legend()
plt.show()