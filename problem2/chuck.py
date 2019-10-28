import requests
import random


def joke_category(category: str) -> str:
    resp = requests.get(f'https://api.chucknorris.io/jokes/random?category={category}')
    if resp.status_code != 200:
        return None
    
    json_resp = resp.json()
    
    return json_resp['value']
    
    


def joke_search(query: str) -> str:
    resp = requests.get(f'https://api.chucknorris.io/jokes/search?query={query}')
    if resp.status_code != 200:
        return None

    json_resp = resp.json()
    
    count = json_resp['total']

    if count == 0:
        return None

    return random.choice(json_resp['result'])
