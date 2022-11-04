import pandas as pd
import numpy as np
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
df=diamonds
print(df)
mask=pd.isnull(df['z'])
print(mask)
print(df[mask])
print(df[df.cut=='NaN'])
    