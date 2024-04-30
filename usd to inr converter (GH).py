import requests
def convert_usd_to_inr(amount):
        # api link for dollar to rupee converter
        url=f'https://open.er-api.com/v6/latest/USD'
        try:
            # sending get request for usd to inr converter
            response=requests.get(url)
            data=response.json()
            # if response is 200 it means api is fine and server is working properly
            if response.status_code==200:
                #extracting the data ( exchange value for usd into inr)
                exchange_rate=data['rates']['INR']
                converted_amount=amount*exchange_rate
                return round(converted_amount,2)
            else:
                # printing that response errorcode.if its not 200(an error is there)
                print(f"unable to convert dollar to INR,error code:{response.status_code}")
                
        except Exception as response:
                han
