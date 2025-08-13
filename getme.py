import requests
from settings import token


BASE_URL = f'https://api.telegram.org/bot{token}'

getme_url = f'{BASE_URL}/getMe'
response = requests.get(getme_url)

print(response.json())
