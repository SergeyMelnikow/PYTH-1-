with open('input.txt','r',encoding="utf-8") as f:
    a=f.readlines()
    b=[x.rstrip().split() for x in a]
    b=sorted(b, key = lambda x:(int(x[2])))
    print(b)
for  j in range(9,12):   
    k=0
    s=0
    for i in range(len(b)):
        if int(b[i][2])==j:
            k=k+1
            s=s+int(b[i][3])
    if k>0:
         print(s/k)
    else: print(0)
    