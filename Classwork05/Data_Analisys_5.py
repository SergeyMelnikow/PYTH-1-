import numpy as np
import matplotlib
from matplotlib import pyplot as plt

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

plt.xlabel("ось X")
plt.ylabel("ось Y")
b,k=np.polynomial.polynomial.polyfit(x,y,deg=1)
x1=np.linspace(-5,15,100)
y1=k*x1+b
print(k,b)
plt.plot(x1,y1,label='polyfit')
plt.scatter(x,y,s=1)
 
k1=(((x*y).mean()-(x.mean())*(y.mean()))/((x*x).mean()-(x.mean())**2))
b1=y.mean()-k1*x.mean()
print(k1,b1)
x2=np.linspace(-5,15,100)
y2=np.array([k1*i+b1 for i in x2])
print(x2,y2)
plt.plot(x2,y2,'r--',label='по МНК')

plt.legend()

plt.show()