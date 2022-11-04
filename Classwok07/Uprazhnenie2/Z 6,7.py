import pandas as pd
import numpy as np
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
df=diamonds
k=0
for i in df.columns:
    mask=pd.isnull(df[i])
    for j in range(len(df)):
        if mask.iloc[j]=='True':
            k+=1
print(k)
print("Пропущенных значений нет")