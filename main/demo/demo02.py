from main.utils import dictUtil
from xtquant import xtdata

# a= dictUtil.getAllModule()
#
# b= dictUtil.getAllStock()
#
# c= dictUtil.getAllStockMain()


# 获取历史行情数据
# history_data = xtdata.get_market_data(field_list=['open', 'close', 'high', 'low', 'volume'],
#                                       stock_list=['000001.SZ'],
#                                       period='1d',
#                                       start_time='20230101',
#                                       end_time='20231115')



# financial_data = xtdata.get_financial_data('600519.SH', ['revenue', 'net_profit'], report_period='annual', start_year=2020, end_year=2023)


# data = xtdata.get_history_data('600519.SH', ['open', 'high', 'low', 'close'], start_date='2023-01-01', end_date='2024-10-11')

# ll=list['600519.SH']
# aaa=xtdata.get_full_tick(ll)


asdf=xtdata.get_instrument_detail('600519.SH', False)


print(1)