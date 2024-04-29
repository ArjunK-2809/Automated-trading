# function for handling various types of errors
def handle_error(response):
    status_code=response.status_code
    if status_code==400:
        print("bad request-your request is invalid")
    if status_code==401:
        print("unauthorized-your api code is wrong")
    elif status_code==404:
        print("Not found-the specific link could not be found")
    elif status_code==429:
        print("too many requests-you are making too many api calls")
    elif status_code==500:
        print("internal server error-we had a problem with our server.try again later")
    elif status_code==503:
        print("service unavailable-we are temporarily offline for maintenance.try again later")
    else:
        print(f"an unexpected error occurred with status code:{status_code}")
