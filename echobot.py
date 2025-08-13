from time import sleep
import requests
from settings import TOKEN


BASE_URL = f'https://api.telegram.org/bot{TOKEN}'

def get_updates(offset: int | None):
    params = {
        'offset': offset
    }
    getupdates_url = f'{BASE_URL}/getUpdates'
    response = requests.get(getupdates_url, params=params)

    return response.json()["result"]


def send_message(chat_id: int, text: str):
    params = {
        'chat_id': chat_id,
        'text': text
    }

    sendmessage_url = f'{BASE_URL}/sendMessage'
    requests.get(sendmessage_url, params=params)


def updater(token: str):

    offset = None

    while True:

        updates = get_updates(offset)

        for update in updates:
            
            if 'message' in update and 'text' in update['message']:
                user = update['message']['from']
                
                send_message(user['id'], update['message']['text'])

            offset = update['update_id'] + 1

        sleep(1)

if __name__ == '__main__':
    updater(TOKEN)
