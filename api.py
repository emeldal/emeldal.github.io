"""Testing web APIs with HTTP GET method"""

import json
import sys
import requests
def print_api(phrase):
    url = "https://webit-text-analytics.p.rapidapi.com/key-phrases"

    querystring = {"language":"fr","q":phrase}

    payload = ""
    headers = {
        'x-rapidapi-host': "webit-text-analytics.p.rapidapi.com",
        'x-rapidapi-key': "f00443d856mshef111d13f0d92bbp17c375jsn86f42c1b92b1",
        'content-type': "application/x-www-form-urlencoded"
        }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    print(response.text)

print_api ("Je vais en Russie.")
