a=[set(i) for i in input().split()]
c=a[0]
for i in range(len(a)):
    c.intersection_update(a[i])
print(c)