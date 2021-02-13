import pandas as pd

a=pd.read_csv('closeprice.csv', encoding='gbk', dtype={'ticker': str})
print(a)

a.to_excel('closeprice.xls')

a=pd.read_csv('closeprice.csv', encoding='gbk')
print(a.describe().T)

print(a.info())

b={1:'银行',2:'房地产',4:'医药生物',5:'房地产',6:'采掘',7:'休闲服务',8:'机械设备'}

a['ind']=a.ticker.map(b)

print(a)

data = pd.DataFrame({'group': ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'], 'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
data.sort_values(by=['group','ounces'], ascending=[False, True], inplace=True)

print(data)