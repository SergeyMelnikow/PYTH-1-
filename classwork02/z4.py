with open('input.txt','r') as f:
    a=f.readlines()
    for i in range(len(a)):
        a[i]=a[i].strip('\n')
    for i in range(len(a)):
        print(a[-1-i])