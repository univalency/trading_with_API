import hmac
import time
import hashlib
import requests
import json
from urllib.parse import urlencode

""" This script works with Binance API on main net

There are different parameters for different endpoints, a full list can be found here:
https://binance-docs.github.io/apidocs/#change-log

```
"""

#You need to insert your keys here:
KEY = ''
SECRET = ''

base_url = 'https://api.binance.com' # base url


''' Now we define functions for passing timestamps, signature, etc.'''

def hashing(query_string):

    return hmac.new(SECRET.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

def dispatch_request(http_method):
    session = requests.Session()
    session.headers.update({
        'Content-Type': 'application/json;charset=utf-8',
        'X-MBX-APIKEY': KEY
    })
    return {
        'GET': session.get,
        'DELETE': session.delete,
        'PUT': session.put,
        'POST': session.post,
    }.get(http_method, 'GET')


def get_timestamp():
    return int(time.time() * 1000)


# sending requests with the signature
def signed_request(http_method, url_path, payload={}):
    query_string = urlencode(payload)
    query_string = query_string.replace('%27', '%22')

    if query_string:
        query_string = "{}&timestamp={}".format(query_string, get_timestamp())
    else:
        query_string = 'timestamp={}'.format(get_timestamp())

    url = base_url + url_path + '?' + query_string + '&signature=' + hashing(query_string)
    print("{} {}".format(http_method, url))
    params = {'url': url, 'params': {}}
    response = dispatch_request(http_method)(**params)
    return response.json()

# public data endpoints
def public_request(url_path, payload={}):
    query_string = urlencode(payload, True)
    url = base_url + url_path
    if query_string:
        url = url + '?' + query_string
    print("{}".format(url))
    response = dispatch_request('GET')(url=url)
    return response.json()


#Now we just include example requests.



#print order book for a particular pair, BTCUSDT

request1 = public_request('/api/v3/depth' , {"symbol": "BTCUSDT"})
print(request1)

#post a new order with parameters as described

params11 = {
        "symbol": "ETHUSDT",
        "type": "LIMIT",
        "side": "BUY",
        "quantity": 0.005,
        "price": "2620",
        "timeInForce": "GTC",
        'newClientOrderId': 1,
        }
signed_request('POST', '/api/v3/order', params11)

