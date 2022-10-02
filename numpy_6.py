import numpy as np
a=np.array([i for i in range(1,100)])
a=np.array([sum(row) for row in a.reshape(33,3)])
a=a.reshape(11,3)
a=a.T
b=np.array([i for i in range(-9,2)]).reshape(11,1)
print(np.matmul(a,b))