import schedule
import time
from module import *


names = ["SG"]
PERCENGTAGE_SELL_TRAILING_STOP = 2

def tradeIpo():
    print("\n" + getTimeNow())
    for NAME in names:
        is_stock_have_share, share_hold = stock_have_share(NAME)
        print("share:",is_stock_have_share, " quatity:", share_hold)
        if is_stock_have_share:
            stockSelltrailingStop(NAME, share_hold, PERCENGTAGE_SELL_TRAILING_STOP)
        
tradeIpo()
schedule.every(10).seconds.do(tradeIpo)
while True:
    schedule.run_pending()
    time.sleep(1)


