def task1():
        a = int(input())
        b = int(input())
        c = (a + b) ** 2
        return (c)

def task2():
        a = (input())
        c = 0
        for i in a:
                if 96 < ord(i) < 123:
                        c = c + 1
        return (c)

def task3():
        a = (input())
        b = a.split()
        c = 0
        for i in b:
                if i[len(i) - 3:] == 'bus':
                        c = c + 1
        return (c)


def task4(generator):
        c = list(filter(lambda x: 'usu' not in x, generator))
        return (c)

def task5(list_of_smth):
        b = []
        for i in range(len(list_of_smth)):
                if len(list_of_smth) - 2 >= i >= 5 and i % 2 == 0:
                        b.append(list_of_smth[i])
        return (b)

def task6(list1, list2, list3, list4):
        a,b,c,d = list1, list2, list3, list4
        a, b, c, d = set(a), set(b), set(c), set(d)
        return ((a.union(d)).intersection(b.union(c)))

def task7():
        import numpy as np
        np.random.seed(9)
        a = np.random.randint(20, size=25)
        b = a.reshape(5, 5)
        c = np.linalg.det(b[1::, :4:])
        return (b, c)

def task8(f, min_x, max_x, N, min_y, max_y):
        import numpy as np
        import matplotlib.pyplot as plt
        x = np.linspace(min_x, max_x, N)
        y = np.array([f(i) if (min_y) < f(i) < (max_y) else 0 for i in x])
        plt.plot(x, y, '-r')
        plt.yscale('log')
        plt.grid()
        plt.savefig('function.jpg')

        y1 = np.array([(f(x[i + 1]) - f(x[i])) / ((x[i + 1]) - (x[i])) if (min_y) < f(i) < (max_y) else 0 for i in
                       range(len(x) - 1)])
        y1 = np.append(y1, y1[len(y1) - 1])
        plt.plot(x, y1)
        plt.show()

def task9(data, x_array, y_array, threshold):
    # TODO: ...

def task10(list_of_smth, n):
        import numpy as np
        a=list_of_smth
        b = []
        for i in range(len(a)):
                b.append((np.array(a[:i] + a[i + 1:])).mean())
        return (b)

def task11(filename="infile.csv"):
    # TODO: ...

def task12(filename="video-games.csv"):
    # TODO: ...
