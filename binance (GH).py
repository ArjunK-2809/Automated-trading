import requests
# code for binance
def get_price_from_binance(symbol):
    # api link for binance
    url='https://api.binance.com/api/v3/ticker/price'
    # parametres for the api request
    parametres={'symbol':symbol}
    # get request to that api
    response=requests.get(url,paramtres=paramtres)
    data=response.json()
    # returning the price from json response
    return float(data['price'])
# all the three coins symbols
symbols=['ETHUSDT','BTCUSDT','FILUSDT']
prices_binance={}
for symbol in symbols:
    # assinging the value we got form binance to variable named price
    price=get_price_from_binance(symbol)
    # converting the value from usd to inr
    price_inr=round(convert_usd_to_inr(price),2)
    #editing those symbols by removing last 4 characters
    prices_binance[symbol[:-4]]=price_inr
# we should change the symbol for BTC to btcinr because we should maintain same symbols across the three companies.
if "BTC" in prices_binance :
            prices_binance["btcinr"]=prices_binance.pop("BTC")
if "ETH" in prices_binance :
            prices_binance["ethinr"]=prices_binance.pop("ETH")
if "FIL" in prices_binance:
            prices_binance["filinr"]=prices_binance.pop("FIL")
