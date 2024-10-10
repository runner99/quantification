from main.utils import dictUtil
from xtquant import xtdata

# a= dictUtil.getAllModule()
#
# b= dictUtil.getAllStock()
#
# c= dictUtil.getAllStockMain()


# 获取历史行情数据
history_data = xtdata.get_market_data(field_list=['open', 'close', 'high', 'low', 'volume'],
                                      stock_list=['000001.SZ'],
                                      period='1d',
                                      start_time='20230101',
                                      end_time='20231115')

print(1)