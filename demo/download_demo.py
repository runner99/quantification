from utils.download_util import *

if __name__ == '__main__':

    # period_list=['1m']
    # start_time='20220101000000'
    # # end_time='20150101000000'
    # end_time='20230101000000'
    #
    # download_allStock(period_list=period_list,start_time=start_time,end_time=end_time)

    download_history('002415.SZ','1d','20241120000000','20241126000000')
