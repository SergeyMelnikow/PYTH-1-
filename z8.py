with open('input.txt','r',encoding="utf-8") as f:
    a=f.readlines()
    b=[x.rstrip().split() for x in a]
    b=sorted(b, key = lambda x:(x[0]))
    for i in range(len(b)):
        print(b[i][0],b[i][1],b[i][3])