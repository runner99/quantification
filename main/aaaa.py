# import random
# from xtquant.xttype import StockAccount
# from xtquant.xttrader import XtQuantTrader
# from xtquant import xtconstant
#
# # miniQMT安装路径
# mini_qmt_path = r'D:\国金证券QMT交易端\userdata_mini'
#
# # QMT账号
# account = '8882282018'
#
# # 创建session_id
# session_id = int(random.randint(100000, 999999))
#
# # 创建交易对家
# xt_trader = XtQuantTrader(mini_qmt_path, session_id)
#
# # 启动交易对家
# xt_trader.start()
#
# # 连接客户端
# connect_result = xt_trader.connect()
#
# if connect_result == 0:
#     print("连接成功")
#
# # 创建账号对家
# acc = StockAccount(account)
#
# # 订阅账号
# xt_trader.subscribe(acc)
#
# # 下单
# res = xt_trader.order_stock(acc, stock_code='600000.SH',
#                             order_type=xtconstant.STOCK_BUY,
#                             order_volume=100,
#                             price_type=xtconstant.FIX_PRICE,
#                             price=7.44)
#
# print(res)
#
#
#
#
#
#








import random
from xtquant.xttype import StockAccount
from xtquant.xttrader import XtQuantTrader
from xtquant import xtconstant

# 请替换以下变量为你的个人信息
mini_qmt_path = 'D:\\国金证券QMT交易端\\'  # 例如：'D:\\国金证券QMT交易端\\'
account = '8882282018'  # 例如：'1010573943'
stock_code = '600519.SH'  # 股票代码，例如：'600519.SH'（贵州茅台）
order_volume = 100  # 下单数量
price = 7.44  # 下单价格

# 创建session_id
session_id = int(random.randint(100000, 999999))

# 创建交易对象
xt_trader = XtQuantTrader(mini_qmt_path, session_id)

# 启动交易对象
xt_trader.start()

# 连接客户端
connect_result = xt_trader.connect()

if connect_result:
    print("连接成功")
else:
    print("连接失败")
    # 如果连接失败，退出程序
    exit()

# 创建账号对象
acc = StockAccount(account)

# 订阅账号
xt_trader.subscribe(acc)

# 下单购买股票
# order = xt_trader.order_stock(acc, stock_code, xtconstant.STOCKBUY, order_volume, xtconstant.MARKET_PRICE)
order = xt_trader.order_stock(acc, stock_code, xtconstant.STOCK_BUY, order_volume, xtconstant.market_p)

# 检查下单结果
if order:
    print("下单成功")
else:
    print("下单失败")

# 这里可以添加更多的交易逻辑，例如设置止损、止盈等
