import matplotlib.pyplot as plt
import pandas as pd
from xtquant import xtdata


stock = '588400.SH'

# 定义股票代码、周期、开始时间和结束时间
stock_code = stock
period = '1m'
start_time = '20000101'
end_time = '20241231'

# 获取本地数据
history_data = xtdata.get_local_data(field_list=[], stock_list=[stock_code], period=period, start_time=start_time,
                                     end_time=end_time, count=-1, dividend_type='none', fill_data=True)

df = history_data[stock_code]
# 将数据转换为Pandas DataFrame
print(df)

# 将时间戳转换为日期格式
df['time'] = pd.to_datetime(df['time'], unit='ms')

# 设置图表大小
plt.figure(figsize=(10, 6))

# 绘制开盘价折线图
plt.plot(df['time'], df['open'], label='Open Price', marker='o')

# 绘制最高价折线图
plt.plot(df['time'], df['high'], label='High Price', marker='o')

# 设置图表标题和坐标轴标签
plt.title('Stock Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price')

# 显示图例
plt.legend()

# 格式化x轴日期显示
plt.gcf().autofmt_xdate()

# 显示图表
plt.show()