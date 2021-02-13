import pandas as pd

a=pd.read_csv('closeprice.csv', encoding='gbk')
print(a)

b = a.drop(['Unnamed: 0'], axis=1)
print(b)

c = a.drop(['Unnamed: 0'], axis='columns')
print(c)