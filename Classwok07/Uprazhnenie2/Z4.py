import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
df=diamonds
df.groupby(['cut']).agg({'price':'mean'}).sort_values(by="price").plot(kind='bar')
