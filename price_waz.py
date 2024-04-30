import requests

# API  for fetching prices
url_waz = 'https://api.wazirx.com/api/v2/tickers'

# Coin symbols
coins_waz = ['btcinr', 'ethinr', 'filinr']

# Fetching prices
try :
 response = requests.get(url_waz)
 data_waz = response.json()
except Exception as response :
    

price_waz= {}
for element in data_waz:
#element will give name of coin 
    if element in coins_waz:
        coin_symbol = element
        last_price = data_waz[element]["last"]
        price_waz[coin_symbol] = last_price
        
print(price_waz)
