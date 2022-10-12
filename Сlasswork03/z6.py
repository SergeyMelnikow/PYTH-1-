D={i:chr(i) for i in range(97,123)}
for i in range(len(D)):
    D[i+1]=D[i+97]
    del D[i+97]
print(D)
W=set(input())
C=0
for i in W:
    for j in D.keys():
        if i == D[j]:
            C=C+j            
print(C)        