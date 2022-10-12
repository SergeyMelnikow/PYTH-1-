D={i:chr(i) for i in range(97,123)}
for i in range(len(D)):
    D[i+1]=D[i+97]
    del D[i+97]
print(D)    