import pandas as pd
import numpy as np
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
df=diamonds
new_df=df.select_dtypes(include=np.number)
for i in new_df.columns:
    print(i,df[i].mean())