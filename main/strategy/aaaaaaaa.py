# 导入需要的库
import numpy as np

# 定义年份和GDP数据
t = np.array([2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021])
y = np.array([4.6, 5.1, 6.1, 7.6, 8.5, 9.6, 10.5, 11.1, 11.2, 12.3, 13.9, 14.3, 14.7, 17.8])

# 计算平均值
t_mean = np.mean(t)
y_mean = np.mean(y)

# 计算斜率k
numerator = np.sum((t - t_mean) * (y - y_mean))
denominator = np.sum((t - t_mean) ** 2)
k = numerator / denominator

# 计算截距b
b = y_mean - k * t_mean

# 输出结果
print(f"斜率 k = {k:.4f}")
print(f"截距 b = {b:.2f}")
