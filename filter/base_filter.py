from loguru import logger

class BaseFilter:
    def __init__(self):
        self.order = 0

    def filter(self, data):
        my_dict={}
        data_dict={}
        data_dict['stock']=data
        my_dict['data']=data_dict
        my_dict['flag'] = True

        # 日线范围
        my_dict['day_range'] = 3

        logger.info(f"BaseFilter filter called with data: {my_dict}")
        return my_dict

