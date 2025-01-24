import decimal
from decimal import Decimal
from xtquant import xtdata
import utils.download_util as download_util
import utils.dict_util as dict_util


class Account:
    def __init__(self, money: Decimal, threshold: Decimal):
        self.money = money
        self.quantity = Decimal(0)
        self.price = None
        self.threshold = threshold

    def is_trade(self, current_price: Decimal):
        if self.price is None:
            multiply = current_price * Decimal(100)
            divide = self.money / Decimal(2)
            big_decimal = divide // multiply

            self.price = current_price
            self.quantity = big_decimal * 100
            self.money -= big_decimal * multiply

            return

        abs_diff = abs(self.price - current_price) * Decimal(100) / self.price
        if abs_diff >= self.threshold:
            self.trade(current_price)

    def trade(self, current_price: Decimal):
        current_stock_total = current_price * Decimal(self.quantity)
        if self.money > current_stock_total:
            divide = (current_stock_total + self.money) / Decimal(2)
            subtract = divide - current_stock_total
            change_count = subtract // (current_price * Decimal(100))

            if change_count > 0:
                self.quantity += change_count * 100
                self.price = current_price
                self.money -= change_count * Decimal(100) * current_price

        elif self.money < current_stock_total:
            divide = (current_stock_total + self.money) / Decimal(2)
            subtract = current_stock_total - divide
            change_count = subtract // (current_price * Decimal(100))

            if change_count > 0:
                self.quantity -= change_count * 100
                self.price = current_price
                self.money += change_count * Decimal(100) * current_price


def build_lines(stock_code: str):

    period = '1d'
    start_time = '20220101'
    end_time = '20221231'

    # 获取本地数据
    history_data = xtdata.get_local_data(field_list=[], stock_list=[stock_code], period=period, start_time=start_time,
                                         end_time=end_time, count=-1, dividend_type='none', fill_data=True)

    df = history_data[stock_code]
    # 将数据转换为Pandas DataFrame
    return df['close'].tolist()


def main():
    allStock = dict_util.getAllStock()

    success=0
    fail=0


    for stock in allStock:
        lines = build_lines(stock_code=stock)

        if len(lines) <=0:
            continue

        init_money = Decimal(20000)
        init_range = Decimal(3)
        account = Account(init_money, init_range)

        for current_price in lines:
            account.is_trade(Decimal(str(current_price)))

        last_price = Decimal(str(lines[-1]))
        if ((account.money + last_price * account.quantity - init_money) / init_money) * 100>(last_price - Decimal(str(lines[0]))) / Decimal(str(lines[0])) * 100:
            success+=1
        else:
            fail+=1

    # print(f"strategy:{init_money} ,end money:{account.money + last_price * account.quantity},rate:{((account.money + last_price * account.quantity - init_money) / init_money) * 100}")
    # print(f"stock: {(last_price - Decimal(str(lines[0]))) / Decimal(str(lines[0])) * 100:.2f}%")
    print(1)

if __name__ == "__main__":
    main()
