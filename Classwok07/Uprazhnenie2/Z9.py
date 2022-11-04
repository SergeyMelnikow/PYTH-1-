import pandas as pd
import numpy as np
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
df=diamonds
np.random.seed(10)
def Func():
    a=np.random.randint(len(df),size=20)
    for i in a:
        return(df.iloc[list(a)])
print(Func())
    
    
    
    