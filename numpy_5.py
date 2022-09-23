import numpy as np
a=np.array([i for i in range(1,100)])
a=(a[::3]).reshape(11,3)
a=a.T
print(a)