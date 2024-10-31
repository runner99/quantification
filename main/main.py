from filter.base_filter import *
from filter.output import *
from strategy.strategy_demo import *
from strategy.download_day import *

from utils import dict_util
from loguru import logger
import time
from datetime import datetime


def call_filters(data):
    base_instance = BaseFilter()
    subclasses = [cls() for cls in BaseFilter.__subclasses__()]
    sorted_subclasses = sorted(subclasses, key=lambda x: x.order)

    result = base_instance.filter(data)

    for subclass in sorted_subclasses:
        result = subclass.filter(result)
        if result['flag'] is not None and result['flag'] == False:
            logger.warning(f"strategy is fail or error: {subclass}")
            break

    return result

def start_filter():
    start_time = time.time()

    result_list=[]
    all = dict_util.getAllStock()
    for item in all:
        stock=call_filters(item)
        if stock['flag']:
            result_list.append(stock)


    end_time = time.time()
    total_time = end_time - start_time
    average_time = total_time / len(all) if all else 0

    logger.info(f"start_time: {datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')},end_time: {datetime.fromtimestamp(end_time).strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info(f"Total time taken: {total_time:.2f} seconds,Total size:{len(all) if all else 0},Average time per item: {average_time:.3f} seconds")



if __name__ == '__main__':
    start_filter()