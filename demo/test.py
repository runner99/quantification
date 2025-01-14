import utils.download_util as download_util
import utils.dict_util as dict_util
from loguru import logger

from datetime import datetime, timedelta

if __name__ == '__main__':

    # for stock in allStock:
    # period_list=['1m']
    # download_util.download_allStock(period_list=period_list)

    start_year = 2025
    current_year = start_year

    period_list=['1m']

    # 循环打印每年的起始时间
    while current_year < 2027:  # 假设我们只打印到2024年
        # 构建日期对象
        start_date = datetime(current_year, 1, 1)

        end_date = datetime(current_year, 12, 31)

        download_util.download_allStock(period_list=period_list,start_time=start_date.strftime('%Y%m%d%H%M%S'),end_time=end_date.strftime('%Y%m%d%H%M%S'))

        # 增加年份
        current_year += 1

