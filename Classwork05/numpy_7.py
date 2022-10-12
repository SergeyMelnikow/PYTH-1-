import numpy as np
np.random.seed(1)
a=np.random.rand(120)
a=a.reshape(12,10)
b=a.min(axis=1)
c=a.max(axis=1)
maxnumbers=[]
minnumbers=[]
for j in range(12):
    for i in range(10):
        if a[j,i]==b[j]:
            maxnumbers.append(i)
        elif a[j,i]==c[j]:
            minnumbers.append(i)
print(maxnumbers)
print(minnumbers)