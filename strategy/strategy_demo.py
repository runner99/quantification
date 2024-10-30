from filter.base_filter import BaseFilter
from loguru import logger

class SubClass2(BaseFilter):
    def __init__(self):
        super().__init__()
        self.order = 2

    def filter(self, data):
        logger.info(f"SubClass2 filter called: {data['data']['stock']}")
        return data