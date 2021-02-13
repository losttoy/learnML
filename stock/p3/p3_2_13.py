import pandas as pd
# 前五条
df = pd.read_csv('20170930.csv', dtype={'ticker': str, 'holdingTicker':str, }, encoding='GBK')
print(df.head())
# 前五条（过滤列）
df = df[['ticker', 'holdingTicker', 'marketValue', 'industryName1']]
print(df.head())

print("基金按ticker分组")
print("全量")
print(df[['holdingTicker']])
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x1210cab00>
print("按ticker分组")
print(df[['holdingTicker']].groupby(df['ticker']))
print("按ticker分组（数量）")
print(df[['holdingTicker']].groupby(df['ticker']).count())
print("按ticker分组（数量-尾巴五个）")
print(df[['holdingTicker']].groupby(df['ticker']).count().tail())

print("基金按行业分组后汇总holdingTicker个数")
print(df[['holdingTicker']].groupby(df['industryName1']).count().sort_values('holdingTicker', ascending=False).head())

print("基金按ticker分组后汇总市值")
print(df[['marketValue']].groupby(df['ticker']).sum().sort_values('marketValue', ascending=False).head())

def t_range(arr):
    return arr.max() - arr.min()

print("基金按ticker分组后汇总最大值和最小值的差异")
print(df[['marketValue']].groupby(df['ticker']).agg(t_range).head())
print("基金按ticker分组后汇总sum/max/min/差异")
print(df[['marketValue']].groupby(df['ticker']).agg(['sum', 'max', 'min', t_range]).head())

#
print("不同的列应用不同的函数")
print(df[['marketValue', 'industryName1']].groupby(df['ticker']).agg ({'marketValue':[t_range],  'industryName1':['count']}).head())

print("选择ticker下前3")
print(df.groupby('ticker').apply(lambda x: x[:3]))
print("选择ticker下前3（限制条数）")
print(df.groupby('ticker').apply(lambda x: x[:3]).head(6))
