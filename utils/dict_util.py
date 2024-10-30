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
    TODO 需要验证返回的基金是否都能买

    conditions = ["ETF", "基金"]

    etf_or_fund_sectors = [sector for sector in allmodule if any(cond in sector for cond in conditions)]

    正式环境：
    沪市ETF:576
    沪市基金:726
    沪深ETF:988
    沪深基金:1506
    深市ETF:412
    深市基金:780

    模拟环境：
    沪市ETF:589
    沪市基金:739
    沪深ETF:1001
    沪深基金:1519
    深市ETF:412
    深市基金:780
    '''
    return xtdata.get_stock_list_in_sector('沪深基金')

