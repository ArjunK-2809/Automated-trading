import requests

# API  for fetching prices
url_dcx = 'https://api.coindcx.com/exchange/ticker'

# Coin symbols
coins_dcx = ['BTCINR', 'ETHINR', 'FILINR']

# Fetching prices and handling errors 
try :
 response = requests.get(url_dcx)
 data_dcx = response.json()
except Exception as response :
        handle_error(response)

#taking price of desired three coins from data 
price_dcx = {}
for element in data_dcx:
#here  in case of coindcx element will give a dict cointaining name of coin and all other terms 
    if element['market'] in coins_dcx:
#element[market] will give name of coin
        coin_symbol = element['market']
        last_price = float(element['last_price'])
#converting symbol into lowercase so that we can compare between other exchanges
        price_dcx[coin_symbol.lower()] = last_price

#printing price of all three coins in form of dict
print(price_dcx)
