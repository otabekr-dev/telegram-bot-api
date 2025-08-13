import requests
from settings import token


BASE_URL = f'https://api.telegram.org/bot{token}'
text = input('enter: ')
params = {
    'chat_id': 5363692421,
    'text': text
}

sendmessage_url = f'{BASE_URL}/sendMessage'
response = requests.get(sendmessage_url, params=params)
