import json
import sys
import requests
def print_api(data):

    url = "https://rapidapi.p.rapidapi.com/entities/recognition/general"

    payload = "{\"documents\": [{\"id\": \"1\",\"language\": \"fr\",\"text\": \""+data+"\"},]}"
    headers = {
        'content-type': "application/json",
        'x-rapidapi-host': "microsoft-text-analytics1.p.rapidapi.com",
        'x-rapidapi-key': "f00443d856mshef111d13f0d92bbp17c375jsn86f42c1b92b1"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
print_api("I went to Seattle.")
