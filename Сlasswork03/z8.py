s=input()
i=0
for i in range(10):
    s=s.replace(str(i),'')
s=s.split()
s=''.join(s)
d = dict()
for i in s:
    if i in d:
        d[i] += 1/len(s)
    else:
        d[i] = 1/len(s)
print(d)