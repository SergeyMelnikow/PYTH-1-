import matplotlib
from matplotlib import pyplot as plt
import numpy as np

matplotlib.rcParams.update(matplotlib.rcParamsDefault)


def get_numbers(student):
    return student, (student + 4) % 5 + 3, student % 2 * 10 + 12, (student % 5 * 3 + 7) * 3 

def fake_data_generator(seed, vmin=0, vmax=10, size=100):
    import numpy as np
    np.random.seed(seed)
    data = np.random.randint(vmin, vmax, size=20)
    mean = data.mean()
    std = data.std()
    noise = np.random.normal(loc=mean, scale=std**.5, size=size)
    fake_x = np.array([-5 + i * 20 / size for i in range(size)])
    
    linear = lambda x, k=(.5 - np.random.rand()) * 15, b=np.random.rand()*10: k * x + b
    linear_data = linear(fake_x)
    fake_y = linear_data + noise
    return fake_x, fake_y
student = 9
x, y = fake_data_generator(*get_numbers(student))

plt.scatter(x,y,s=2,label='DATA')
plt.grid()

print(x.mean(),y.mean())

d=[0.5*(x[i+1]-x[i]) for i in range(len(x)-1)]
d.append(x[len(x)-1]-x[len(x)-2])
d1=np.array(d)
plt.errorbar(x,y,yerr=abs(y)**0.5,xerr=abs(d1),fmt='.')

x1=np.linspace(-10,20,1000)
y1=[y.mean() for i in range(len(x1))]
plt.plot(x1,y1,'r-.',label='mean y = 10.39')

y2=np.linspace(-20,40,1000)
x2=[x.mean() for i in range(len(y2))]
plt.plot(x2,y2,'b--',label='mean x = 4.82')

x3=np.linspace(-10,20,1000)
y3=19-2*x3
plt.plot(x3,y3,'k--',label='fit')

plt.plot(x.mean(),(19-2*x.mean()),'bo')
plt.plot((19-y.mean())/2,y.mean(),'bo')

plt.xlabel(r'$\xi, cm$')
plt.ylabel(r'$\rho, mm^{-3}$')

plt.legend()

plt.show()