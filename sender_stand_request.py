import requests
import configuration
import data

def create_order():
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=data.order_body
    )
    
def get_order(track_number):
    url = configuration.URL_SERVICE + configuration.GET_ORDER_PATH
    params = {"t": track_number}
    return requests.get(url, params=params)
