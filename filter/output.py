from filter.base_filter import BaseFilter
from loguru import logger

class OutPut(BaseFilter):
    def __init__(self):
        super().__init__()
        self.order = 10000

    def filter(self, data):
        # todo 输出到短信或者邮件
        # logger.info(f"output processed {data}")
        return data