import numpy as np
import matplotlib.pyplot as plt

x=np.array([i*10 for i in range(11)])
print(x)
y=np.sin(x)
plt.scatter(x,y,s=1)
plt.show()