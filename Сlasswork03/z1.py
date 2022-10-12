a=input().split()
b=[set(a[i]) for i in range(len(a))]
print(b[0].intersection(b[1].intersection(b[2])))