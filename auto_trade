import pybithumb
import time
import datetime

conkey = "1f43aa68b629139c9ce8bc00255b3568"
seckey = "cf8f62aafbd961f16909e16caace7674"

def get_target_price(ticker, k): #매수 목표가

    df = pybithumb.get_ohlcv(ticker, interval="day",count = 2)   
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):  #시작 시간
    df = pybithumb.get_ohlcv(ticker,interval="day", count = 1)
    start_time = df.index[0]
    return start_time

def get_my_balance(ticker): #내 잔고
    balances = bithumb.get_balance()
    for i in balances:
        if i['currency'] == ticker:
            if i['balance'] is not None:
                return float(i['balance'])
            else:
                return 0
    return 0
            
def get_current_price(ticker):
    return pybithumb.get_orderbook(tickers = ticker)[0]["orderbook_units"][0]["ask_price"]

bithumb = pybithumb.Bithumb(conkey,seckey)
print("auto trade start!")
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(seconds= 10)


        if start_time < now < end_time:
            target_price = get_target_price("KRW-BTC", 0.5)
            current_price = get_current_price("KRW-BTC")
            if target_price < current_price:
                krw = get_my_balance("KRW")
                if krw > 5000:
                    pybithumb.Bithumb.buy_market_order("KRW_BTC", krw*0.9995)
        else:
            btc = get_my_balance("BTC")
            if btc > 0.00008:
                pybithumb.Bithumb.sell_market_order("KRW-BTC", btc*0.9995)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)




