with open('input.txt','r',encoding="utf-8") as f:
    a=f.readlines()
    b=[x.rstrip().split() for x in a]
    b=sorted(b, key = lambda x:(int(x[2]),-int(x[3])))
    print(b[0][3])
for i in range(1,len(b)):
    if b[i][2]!=b[i-1][2]:
        print(b[i][3])