import pandas as pd

print(pd.Series([40, 12, -3, 25]))
print(pd.Series([40, 12, -3, 25]).index)
print(pd.Series([40, 12, -3, 25]).values)

# Series建立的时候就建立索引
print(pd.Series([40, 12, -3, 25], index=['a', 'b', 'c', 'd']))


print(pd.Series([40, 12, -3, 25]).describe())
print(pd.Series([40, 12, -3, 25]).to_dict())