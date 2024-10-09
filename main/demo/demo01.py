from xtquant import xtdata

# 不显示初始化信息
xtdata.enable_hello=False


# 获取所有板块
sectors = xtdata.get_sector_list()
for i in range(0, len(sectors), 6):
    print(" ".join(sectors[i:i+6]))



# 获取沪深A股所有的股票代码
# 主板（上海主板、深圳主板）、科创板、 创业板 、北交所四大板块
stock_list = xtdata.get_stock_list_in_sector('沪深A股')
print(stock_list)


# todo数据待确认
# 获取沪深A股主板代码
def get_mainboard_stocks():
    stock_list = xtdata.get_stock_list_in_sector('沪深A股')
    mainboard_stocks = []
    for stock in stock_list:
        if stock.startswith('600') or stock.startswith('601') or stock.startswith('603') or stock.startswith('605') or stock.startswith('000'):
            mainboard_stocks.append(stock)

    return mainboard_stocks

# 调用函数并打印结果
mainboard_stocks = get_mainboard_stocks()
print("沪深A股主板股票列表:")
for stock in mainboard_stocks:
    print(stock)


print(1)