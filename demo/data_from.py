from utils.download_util import *
import pandas as pd

stock = '002415.SZ'

# 定义股票代码、周期、开始时间和结束时间
stock_code = stock
period = '1m'
start_time = '20241127093000'
end_time = '20241127103000'

download_history(stock_code, period, start_time, end_time)

data = xtdata.get_local_data(field_list=[], stock_list=[stock_code], period=period, start_time=start_time,
                             end_time=end_time, count=-1, dividend_type='none', fill_data=True)

df = pd.DataFrame(data[stock_code])
time = df['time']

print(df)
