import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

titanic = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv")
df=titanic

#Male

#1class
print('male,class 1')
a=df[(df.sex=='male')&(df.pclass ==1)]
df_m11=a.sort_values(by="age").iloc[:(len(a)//2)]
print(len(df_m11[df_m11.survived==1])/len(df_m11))
df_m12=a.sort_values(by="age").iloc[(len(a)//2):]
print(len(df_m12[df_m12.survived==1])/len(df_m12))

#2cass
print('male,class 2')
a=df[(df.sex=='male')&(df.pclass ==2)]
df_m21=a.sort_values(by="age").iloc[:(len(a)//2)]
print(len(df_m21[df_m21.survived==1])/len(df_m21))
df_m22=a.sort_values(by="age").iloc[(len(a)//2):]
print(len(df_m22[df_m22.survived==1])/len(df_m22))

#3cass
print('male,class 3')
a=df[(df.sex=='male')&(df.pclass ==3)]
df_m31=a.sort_values(by="age").iloc[:(len(a)//2)]
print(len(df_m31[df_m31.survived==1])/len(df_m31))
df_m32=a.sort_values(by="age").iloc[(len(a)//2):]
print(len(df_m32[df_m32.survived==1])/len(df_m32))

#Female

#1class
print('female,class 1')
a=df[(df.sex=='female')&(df.pclass ==1)]
df_fm11=a.sort_values(by="age").iloc[:(len(a)//2)]
print(len(df_fm11[df_fm11.survived==1])/len(df_fm11))
df_fm12=a.sort_values(by="age").iloc[(len(a)//2):]
print(len(df_fm12[df_fm12.survived==1])/len(df_fm12))

#2cass
print('female,class 2')
a=df[(df.sex=='female')&(df.pclass ==2)]
df_fm21=a.sort_values(by="age").iloc[:(len(a)//2)]
print(len(df_fm21[df_fm21.survived==1])/len(df_fm21))
df_fm22=a.sort_values(by="age").iloc[(len(a)//2):]
print(len(df_fm22[df_fm22.survived==1])/len(df_fm22))

#3cass
print('female,class 3')
a=df[(df.sex=='female')&(df.pclass ==3)]
df_fm31=a.sort_values(by="age").iloc[:(len(a)//2)]
print(len(df_fm31[df_fm31.survived==1])/len(df_fm31))
df_fm32=a.sort_values(by="age").iloc[(len(a)//2):]
print(len(df_fm32[df_fm32.survived==1])/len(df_fm32))