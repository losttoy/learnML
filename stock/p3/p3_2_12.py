import pandas as pd

a=pd.read_csv('closeprice.csv', encoding='gbk')
bins=[4,9,10,20,30]
cat=pd.cut(a.closePrice,bins)
print(cat)

print(pd.value_counts(cat))

group_names = ['low',  'Middle_1', 'Middle_2', 'high']
print(pd.cut(a.closePrice, bins, labels=group_names))