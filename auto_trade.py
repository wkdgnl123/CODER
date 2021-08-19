import pybithumb
import time
import datetime
from pybithumb.client import Bithumb

conkey = "1f43aa68b629139c9ce8bc00255b3568"
seckey = "cf8f62aafbd961f16909e16caace7674"
bithumb = pybithumb.Bithumb(conkey,seckey)

def get_target_price(ticker, k): #매수 목표가
    df = pybithumb.get_ohlcv(ticker)   
    yesterday = df.iloc[-2]
    today_open = yesterday['close']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    target = today_open + (yesterday_high - yesterday_low) * k
    return target

# def get_start_time(ticker):  #시작 시간
#     df = pybithumb.get_ohlcv(ticker,interval="day")
#     start_time = df.index[0]
#     return start_time


# def get_balance(ticker): #내 잔고
#     balances = Bithumb.get_balances()
#     for b in balances:
#         if b['currency'] == ticker:
#             if b['balance'] is not None:
#                 return float(b['balance'])
#             else:
#                 return 0
#     return 0

def buy_crypto_currency(ticker):
    krw = bithumb.get_balance(ticker)[2]
    orderbook = pybithumb.get_orderbook(ticker)
    sell_price = orderbook['asks'][0]['price']   
    unit = krw/float(sell_price)
    bithumb.buy_market_order(ticker, unit)

def sell_crypto_currency(ticker):
    unit = bithumb.get_balance(ticker)[0]
    bithumb.sell_market_order(ticker, unit)

# def get_current_price(ticker):
#     """현재가 조회"""
#     return pybithumb.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]

now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
target_price = get_target_price("BTC",0.5)
print("auto trade start!")
while True:
    try:
        now = datetime.datetime.now()
        if mid < now < mid + datetime.timedelta(seconds=10): 
            target_price = get_target_price("BTC",0.5)
            mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
            sell_crypto_currency("BTC")

        current_price = pybithumb.get_current_price("BTC")
        if current_price > target_price:
            buy_crypto_currency("BTC")

    except:
        print("에러")
    time.sleep(1)


