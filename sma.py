from binance.client import Client

binance_api_key = 'dummy_api_key'  # Enter your own API-key here
binance_api_secret = 'dummy_api_secret'  # Enter your own API-secret here

client = Client(api_key=binance_api_key, api_secret=binance_api_secret)
print(client.get_symbol_info('BNBBTC'))
klines = client.get_historical_klines("BNBBTC", Client.KLINE_INTERVAL_1MINUTE, "50 min ago UTC")

sum_for_25=0
sum_for_50=0
for i in range(0,24):
    sum_for_25 = sum_for_25 + float(klines[i][4])
sum_for_50 = sum_for_25
for i in range(25,49):
    sum_for_50 = sum_for_50 + float(klines[i][4])

print(sum_for_25/25)
print(sum_for_50/50)

if sum_for_25/25 > sum_for_50/50:
    order = client.order_market_buy(
        symbol='BNBBTC',
        quantity=0.011)