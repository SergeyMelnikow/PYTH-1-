import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

titanic = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv")
df=titanic

df1=df.groupby('age').agg({'survived': 'sum'})
df2=df.groupby('age').agg({'survived': 'count'})
df3=df2
df3['survived']=df1['survived']/df2['survived']

df3.plot(kind='bar',color='lightblue')
plt.ylabel('Доля выживших людей данного возраста')
