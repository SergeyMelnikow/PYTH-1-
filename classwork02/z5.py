with open('input.txt','r') as f:
    a=f.read()
    a=a.split('\n')
    b=[]
    for i in range(len(a)):
        s=''
        for j in range(len(a[-i-1])):
            s=s+a[-i-1][-j-1]
        b.append(s)
    for i in range(len(b)):
        print(b[i])
    