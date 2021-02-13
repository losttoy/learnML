import tushare as ts


def stock_basic():
    pro = ts.pro_api()

    # 查询当前所有正常上市交易的股票列表
    data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    return data
