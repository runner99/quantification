from main.utils import dictUtil
from xtquant import xtdata
import pandas as pd

if __name__ == '__main__':
    allMain = dictUtil.getAllStock()
    for stock in allMain:

        xtdata.download_history_data(stock_code=stock, period='1d', start_time='20230101', end_time='20231231')

        # 定义股票代码、周期、开始时间和结束时间
        stock_code = stock
        period = '1d'
        start_time = '20230101'
        end_time = '20231231'

        # 获取本地数据
        history_data = xtdata.get_local_data(field_list=[], stock_list=[stock_code], period=period, start_time=start_time,
                                             end_time=end_time, count=-1, dividend_type='none', fill_data=True)

        # 将数据转换为Pandas DataFrame
        df = pd.DataFrame(history_data[stock_code])
        print(df)
