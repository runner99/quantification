import matplotlib.pyplot as plt
import pandas as pd
from xtquant import xtdata

# 设置股票代码、周期、开始时间和结束时间
stock_code = '000001.SZ'
period = '1d'  # 日线数据
start_time = '20230101'  # 开始时间
end_time = '20231231'  # 结束时间

# 获取本地股票数据
history_data = xtdata.get_local_data(
    field_list=['close'],  # 获取收盘价字段
    stock_list=[stock_code],
    period=period,
    start_time=start_time,
    end_time=end_time,
    count=-1,
    dividend_type='none',  # 不进行复权处理
    fill_data=True  # 填充缺失的数据
)

# 检查是否成功获取数据
# if history_data.empty:
#     print("No data retrieved.")
# else:
# 提取收盘价数据
close_prices = history_data[stock_code]['close']

# 将日期转换为字符串格式，以便在图表上正确显示
close_prices.index = close_prices.index.strftime('%Y-%m-%d')

# 绘制收盘价图
plt.figure(figsize=(10, 5))  # 设置图表大小
plt.plot(close_prices.index, close_prices, label='Close Price')  # 绘制收盘价线图

# 设置标题和标签
plt.title(f'Daily Stock Price of {stock_code}')
plt.xlabel('Date')
plt.ylabel('Price')

# 显示图例
plt.legend()

# 优化x轴日期标签的显示，避免重叠
plt.gcf().autofmt_xdate()

# 显示图表
plt.show()