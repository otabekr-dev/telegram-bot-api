import requests
from settings import token


BASE_URL = f'https://api.telegram.org/bot{token}'

getupdates_url = f'{BASE_URL}/getUpdates'
response = requests.get(getupdates_url)

print(response.json())
