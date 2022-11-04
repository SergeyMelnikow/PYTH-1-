import pandas as pd
import numpy as np
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
df=diamonds
print(df[(df.x>5) | (df.y>5) | (df.z>5)])