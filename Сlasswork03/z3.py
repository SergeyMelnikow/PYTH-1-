b=[int(i) for i in input().split()]
c=[set() for i in range(len(b))]
for j in range(len(b)):
    while b[j]>0:
        c[j].add(b[j] % 10)
        b[j]=b[j] // 10
a=c[0]       
for i in c:
    a.intersection_update(i)
print(a)                          