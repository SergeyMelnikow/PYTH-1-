import numpy as np
np.random.seed(1)
a=np.random.rand(120)
a=a.reshape(12,10)
print(a,'\n')
print(a.min(axis=0))
print(a.max(axis=0))