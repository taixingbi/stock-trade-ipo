import schedule
import time
from module import *

class Trade:
    def __init__(self):
        self.NAMES = ["SG"]
        self.ORDER_SHARE = 1
        # self.order_share = 560
        self.PERCENGTAGE_BUY_TRAILING_STOP = 1
        self.valid = True

    def job(self):
        print("\n" + getTimeNow())
        for NAME in self.NAMES:
            is_stock_have_share, share_hold = stock_have_share(NAME)
            print("share:", is_stock_have_share, " quatity:", share_hold)
            if is_stock_have_share and self.valid:
            # if self.valid:
                print(NAME, " order is placed")
                stockBuytrailingStop(NAME, self.ORDER_SHARE, self.PERCENGTAGE_BUY_TRAILING_STOP)
                self.valid = False

if __name__ == '__main__':
    Trade = Trade()
    Trade.job()
    schedule.every(3).seconds.do(Trade.job)
    while True:
        schedule.run_pending()
        time.sleep(1)


