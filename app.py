from flask import Flask, jsonify,render_template,request,flash,redirect,url_for,session
import requests
from flask import Flask, send_from_directory

app = Flask(__name__)
app.secret_key = "Arjun"


# Example dictionary
percentage_dic = {
    "BTC": [5.6, "price_binance", "price_wazirx"],
    "ETH": [3.2, "price_dcx", "price_binance"],
    "FIL": [7.1, "price_dcx", "price_binance"]
}

@app.route('/',methods=['POST','GET'])
def index():
    flash("Welcome to automated Trader!")

    # API  for fetching prices
    url_dcx = 'https://api.coindcx.com/exchange/ticker'

    # Coin symbols
    coins = ['BTCINR', 'ETHINR', 'FILINR']

    # Fetching prices
    response = requests.get(url_dcx)
    data = response.json()

    # Parsing and printing prices
    price_dcx = {}
    for item in data:
        if item['market'] in coins:
            coin_symbol = item['market']
            last_price = float(item['last_price'])
            price_dcx[coin_symbol.lower()] = last_price

    print(price_dcx)




    # API endpoint for fetching prices
    url_waz = 'https://api.wazirx.com/api/v2/tickers'

    # Coin symbols
    coins = ['btcinr', 'ethinr', 'filinr']

    # Fetching prices
    response = requests.get(url_waz)
    data = response.json()

    # Parsing and printing prices
    price_wazirx= {}
    for pair, ticker in data.items():
        if pair in coins:
            last_price = float(ticker['last'])
            price_wazirx[pair] = last_price

    print(price_wazirx)


    def convert_usd_to_inr(amount):
        # Replace 'YOUR_API_KEY' with your actual API key
        api_key = 'YOUR_API_KEY'
        url = f'https://open.er-api.com/v6/latest/USD'
        
        try:
            response = requests.get(url)
            data = response.json()
            
            if response.status_code == 200:
                exchange_rate = data['rates']['INR']
                converted_amount = amount * exchange_rate
                return converted_amount
            else:
                print(f"Failed to retrieve data. Status code: {response.status_code}")
                return None
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

    def get_price_from_binance(symbol):
        url = 'https://api.binance.com/api/v3/ticker/price'
        params = {'symbol': symbol}
        response = requests.get(url, params=params)
        data = response.json()
        return float(data['price'])

    symbols = ['ETHUSDT', 'BTCUSDT', 'FILUSDT']
    prices_binance = {}

    for symbol in symbols:
        price = get_price_from_binance(symbol)
        price_inr = round(convert_usd_to_inr(price), 2)
        prices_binance[symbol[:-4]] = price_inr

    if "BTC" in prices_binance :
                prices_binance["btcinr"] = prices_binance.pop("BTC")
    if "ETH" in prices_binance :
                prices_binance["ethinr"] = prices_binance.pop("ETH")
    if "FIL" in prices_binance:
                prices_binance["filinr"] = prices_binance.pop("FIL")
    print(prices_binance)


    max_dict = {}
    min_dict = {}

    for key in price_dcx.keys():
        # Get the maximum value and its source
        max_val, max_source = max([(price_dcx[key], 'price_dcx'), (price_wazirx[key], 'price_wazirx'), (prices_binance[key], 'price_binance')])
        max_dict[key] = (max_val, max_source)
        
        # Get the minimum value and its source
        min_val, min_source = min([(price_dcx[key], 'price_dcx'), (price_wazirx[key], 'price_wazirx'), (prices_binance[key], 'price_binance')])
        min_dict[key] = (min_val, min_source)

    print("Maximum values dictionary:", max_dict)
    
    print("Minimum values dictionary:", min_dict)
    
    
    
    # Initialize dictionary to store percentage difference
    percentage_dict = {}

    # Iterate over keys in the dictionaries again to calculate percentage difference
    for key in price_dcx.keys():
        max_val, _ = max_dict[key]
        min_val, _ = min_dict[key]
        percentage = ((max_val - min_val) / min_val) * 100

        # Add the percentage difference to the new dictionary
        percentage_dict[key] = [percentage,min_dict[key][1],max_dict[key][1]]

    print("Percentage difference dictionary:", percentage_dict)
    

    
    flash(f"Maximum value of Bitcoin is : {max_dict.get('btcinr')[0]} from {max_dict.get('btcinr')[1]}")
    flash(f"Minimum value of Bitcoin is : {min_dict.get('btcinr')[0]} from {min_dict.get('btcinr')[1]}")
    flash(f"Percentage difference of Bitcoin is: {round(percentage_dict.get('btcinr')[0],2)}")
    
    
    flash(f"Maximum value of Filecoin is : {max_dict.get('filinr')[0]} from {max_dict.get('filinr')[1]}")
    flash(f"Minimum value of Filecoin is : {min_dict.get('filinr')[0]} from {min_dict.get('filinr')[1]}")
    flash(f"Percentage difference of Filecoin is: {round(percentage_dict.get('filinr')[0],2)}")
    
    flash(f"Maximum value of Ethereum is : {max_dict.get('ethinr')[0]} from {max_dict.get('ethinr')[1]}")
    flash(f"Minimum value of Ethereum is : {min_dict.get('ethinr')[0]} from {min_dict.get('ethinr')[1]} ")
    flash(f"Percentage difference of Ethereum is: {round(percentage_dict.get('ethinr')[0],2)}")
    return render_template("index.html")






