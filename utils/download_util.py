from datetime import datetime
from xtquant import xtdata
from .dict_util import *
from loguru import logger

xtdata.enable_hello = False


def download_allMainStock(period_list=['1d', '1m'],
                          start_time='20000101000000',
                          end_time=datetime.now().strftime("%Y%m%d%H%M%S")):
    download_allDayAndMin(getAllStockMain(), period_list, start_time, end_time)


def download_allStock(period_list=['1d', '1m'],
                      start_time='20000101000000',
                      end_time=datetime.now().strftime("%Y%m%d%H%M%S")):
    download_allDayAndMin(getAllStock(), period_list, start_time, end_time)


def download_allEtf(period_list=['1d', '1m'],
                    start_time='20000101000000',
                    end_time=datetime.now().strftime("%Y%m%d%H%M%S")):
    download_allDayAndMin(getAllEtf(), period_list, start_time, end_time)


def download_allDayAndMin(stock_list, period_list, start_time, end_time):
    for stock_code in stock_list:
        for period in period_list:
            download_history(stock_code, period, start_time, end_time)


def download_history(stock_code, period, start_time='', end_time=''):
    xtdata.download_history_data(stock_code=stock_code, period=period, start_time=start_time, end_time=end_time)
    logger.info(f'{datetime.now().strftime("%Y:%m:%d %H:%M:%S ")}download history data success:{stock_code},period:{period}')
