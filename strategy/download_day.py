from filter.base_filter import BaseFilter
from utils.download_util import download_history
from datetime import datetime
from xtquant import xtdata

class downloadDay(BaseFilter):
    def __init__(self):
        super().__init__()
        self.order = 1

    def filter(self, data):

        stock=data['data']['stock']
        period='1d'
        start_time='20000101000000'
        end_time=datetime.now().strftime("%Y%m%d%H%M%S")

        download_history(stock,period,start_time,end_time)

        history_data = xtdata.get_local_data(field_list=[], stock_list=[stock], period=period, start_time=start_time,
                                             end_time=end_time, count=-1, dividend_type='none', fill_data=True)

        data['data']['line_day']=history_data[stock]
        return data