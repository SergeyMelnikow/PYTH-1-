import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
df=diamonds
print(df)
plt.hist(df['carat'],'auto')