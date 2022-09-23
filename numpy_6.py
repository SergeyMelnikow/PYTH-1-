import numpy as np
a=np.array([i for i in range(1,100)])
a=(a[::3]).reshape(11,3)
a=a.T
b=np.array([i for i in range(-9,2)]).reshape(11,1)
print(np.matmul(a,b))