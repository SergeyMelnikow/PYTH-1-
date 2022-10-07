import numpy as np
a=np.array([i for i in range(1,100)])
a=np.array([sum(row) for row in a.reshape(33,3)])
a=a.reshape(11,3)
b=np.array([[a[i,j] for j in range(3)] for i in [2,5,8]])
print(np.linalg.det(b))