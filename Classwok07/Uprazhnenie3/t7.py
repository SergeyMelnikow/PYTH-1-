import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

titanic = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv")
df=titanic
print(sum(df['survived']))
df1=df.sort_values(by="age")
df2=df1.groupby('age').agg({'survived':'sum'})
print(df2)
df3=df2*0
for i in df2.index:
    df3['survived'].loc[i]=sum(df2['survived'].loc[:i])
plt.plot(df3/(len(df)),label='куммулятивный график')
plt.xlabel('возраст (x)')
plt.ylabel('суммарная доля выживших возраста<=x')
plt.legend()
plt.show()