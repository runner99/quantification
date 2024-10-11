from xtquant import xtdata

# 不显示初始化信息
xtdata.enable_hello = False

# 获取沪深A股所有的股票代码 包含：主板（上海主板、深圳主板）、科创板、 创业板 、北交所四大板块
stockA_list = xtdata.get_stock_list_in_sector('沪深A股')


def getAllModule():
    '''
    获取A股所有的板块
    '''
    return xtdata.get_sector_list()


def getAllStock():
    '''
    获取A股所有的股票
    '''
    return stockA_list


def getAllStockMain():
    '''
    获取A股所有主板的股票
    TODO 不确定具体的代码格式
    '''
    return [stock for stock in stockA_list if stock.startswith(('60', '000', '002'))]
    # return [stock for stock in stockA_list if stock.startswith(('60', '00'))]
    # return [stock for stock in stockA_list if stock.startswith(('600', '601','603','000','001','002','003'))]


def getAllEtf():
    '''
    获取A股所能买的etf
    TODO
    '''
    return [stock for stock in stockA_list if stock.startswith(('60', '000', '002'))]

def is_array_contained(arr1, arr2):
    for item in arr2:
        if item not in arr1:
            return False
    return True

if __name__ == '__main__':
    allmodule = getAllModule()
    # for stock in allmodule:
    #     print(stock)

    conditions = ["ETF", "基金"]

    etf_or_fund_sectors = [sector for sector in allmodule if any(cond in sector for cond in conditions)]

    result = None

    print(etf_or_fund_sectors)

    for etf in etf_or_fund_sectors:
        aa = xtdata.get_stock_list_in_sector(etf)
        print(etf + ':' + str(len(xtdata.get_stock_list_in_sector(etf))))
        # for stock in aa :
        #     print(stock)

    # array1 = xtdata.get_stock_list_in_sector('沪深基金')
    # array2 = xtdata.get_stock_list_in_sector('深市基金')
    # print(is_array_contained(array1, array2))
    # array1 = [1, 2, 3, 4, 5]
    # array2 = [3, 4]
    # print(is_array_contained(array1, array2))  # True
    #
    # array3 = [6, 7]
    # print(is_array_contained(array1, array3))  # False
    # print(1)




def is_array_contained(arr1, arr2):
    for item in arr2:
        if item not in arr1:
            return False
    return True