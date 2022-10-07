import numpy as np
a=np.array([i for i in range(1,100)])
a=np.array([sum(row) for row in a.reshape(33,3)])
a=a.reshape(11,3)
a=a.T
print(a)
b=np.array([[a[i,j] for j in [1,5,9]] for i in [0,2]])
print(b)