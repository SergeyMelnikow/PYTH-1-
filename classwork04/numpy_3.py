import numpy as np
a=np.array([i for i in range(1,100)])
a=[a[3*i]+a[3*i+1]+a[3*i+2] for i in range(33)]
print(a)
