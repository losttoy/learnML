import pandas as pd
import numpy as np

a=pd.read_csv('closeprice.csv', encoding='gbk')
print(a)

print(a.replace(1, np.nan))

#3.2.10
print(a.rename(columns={'Unnamed: 0':'id'}))

#3.2.11
# location
print(a.loc[:,['ticker','closePrice']])
# integer location
print(a.iloc[:4,[1,4]])
# print(a.ix[:4,['ticker','closePrice']])

print(a[a.closePrice>10])