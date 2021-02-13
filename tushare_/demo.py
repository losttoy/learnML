import datetime

import tushare as ts

from tushare_.basic import stock_basic

ts.set_token('4eea3afc67f115c7cc812079a002fbe5f781bd4422006af90b10211a')


print()


stock_basic().to_excel('stock_basic%s.xlsx'%(datetime.datetime.now().strftime("%Y%m%d %H:%M:%S")))