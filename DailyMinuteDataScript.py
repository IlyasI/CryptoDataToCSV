import cryptodatatocsv
import schedule
import time
import functools

#reusable decorator for logging
def with_logging(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('LOG: Running job "%s"' % func.__name__)
        result = func(*args, **kwargs)
        print('LOG: Job "%s" completed'  % func.__name__)
        return result
    return wrapper

@with_logging
def xmrdailyjob():
    coins = ['BTC', 'ETH', 'XRP', 'BCH', 'LTC', 'DASH', 'XEM', 'NEO', 'BCC', 'XMR']
    for coin in coins:
        print("Saving 1440 Minute "+coin+" to USD Data points to CSV file...")
        cryptodatatocsv.minute_to_csv(crypto=coin, dataPoints=1440)

schedule.every().day.at("14:00").do(xmrdailyjob)
while 1:
    schedule.run_pending()
    time.sleep(1)
