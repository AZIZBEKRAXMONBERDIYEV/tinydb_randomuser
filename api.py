import requests

base_url = "https://randomuser.me/api/"




payload = {
    'results':100,
}

response = requests.get(url=base_url,params=payload)



