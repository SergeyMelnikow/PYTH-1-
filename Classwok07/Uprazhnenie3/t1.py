import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

titanic = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv")
df=titanic

plt.hist(df[df.sex=='male']['age'],'auto',color='b',label='male_age')
plt.hist(df[df.sex=='male']['pclass'],'auto',color='lightblue',label='male_class')

plt.hist(df[df.sex=='female']['age'],'auto',color='purple',label='female_age')
plt.hist(df[df.sex=='female']['pclass'],'auto',color='r',label='female_class')

plt.legend()