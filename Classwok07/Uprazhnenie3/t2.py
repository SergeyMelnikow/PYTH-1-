import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

titanic = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv")
df=titanic

#Male

#1class
a=df[(df.sex=='male')&(df.pclass ==1)]
df_m11=a.sort_values(by="age").iloc[:(len(a)//2)]
df_m12=a.sort_values(by="age").iloc[(len(a)//2):]

#2cass
a=df[(df.sex=='male')&(df.pclass ==2)]
df_m21=a.sort_values(by="age").iloc[:(len(a)//2)]
df_m22=a.sort_values(by="age").iloc[(len(a)//2):]

#3cass
a=df[(df.sex=='male')&(df.pclass ==3)]
df_m31=a.sort_values(by="age").iloc[:(len(a)//2)]
df_m32=a.sort_values(by="age").iloc[(len(a)//2):]

#Female

#1class
a=df[(df.sex=='female')&(df.pclass ==1)]
df_fm11=a.sort_values(by="age").iloc[:(len(a)//2)]
df_m12=a.sort_values(by="age").iloc[(len(a)//2):]

#2cass
a=df[(df.sex=='female')&(df.pclass ==2)]
df_fm21=a.sort_values(by="age").iloc[:(len(a)//2)]
df_fm22=a.sort_values(by="age").iloc[(len(a)//2):]

#3cass
a=df[(df.sex=='female')&(df.pclass ==3)]
df_fm31=a.sort_values(by="age").iloc[:(len(a)//2)]
df_fm32=a.sort_values(by="age").iloc[(len(a)//2):]
