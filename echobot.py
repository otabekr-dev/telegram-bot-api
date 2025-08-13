from time import sleep
import requests
from settings import token


BASE_URL = f'https://api.telegram.org/bot{token}'

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


def send_contact(chat_id: int, first_name: str, phone_number: str):
    params = {
        'chat_id': chat_id,
        'first_name': first_name,
        'phone_number': phone_number,
    }

    sendmessage_url = f'{BASE_URL}/sendContact'
    requests.get(sendmessage_url, params=params)



def send_photo(chat_id: int, photo: str):
    params = {
        'chat_id': chat_id,
        'photo': photo,
    }

    sendmessage_url = f'{BASE_URL}/sendPhoto'
    requests.get(sendmessage_url, params=params)

def send_document(chat_id: int, document: str):
    params = {
        'chat_id': chat_id,
        'document': document
    }

    senddoc_url = f'{BASE_URL}/sendDocument'
    requests.get(senddoc_url, params=params)

def send_audio(chat_id: str, audio: str):
    params = {
        'chat_id': chat_id,
        'audio': audio
    } 

    sendaud_url = f'{BASE_URL}/sendAudio'
    requests.get(sendaud_url, params=params)

def send_voice(chat_id: str, voice: str):
    params = {
        'chat_id': chat_id,
        'voice': voice
    }

    sendv_url = f'{BASE_URL}/sendVoice'
    requests.get(sendv_url, params=params)


def send_animation(chat_id: str, animation: str):

    params = {
        'chat_id': chat_id,
        'animation': animation
    }

    sendanim_url = f'{BASE_URL}/sendAnimation'
    requests.get(sendanim_url, params=params)

def send_video(chat_id: str, video: str):

    params = {
        'chat_id': chat_id,
        'video': video
    }    

    sendvid_url = f'{BASE_URL}/sendVideo'
    requests.get(sendvid_url, params=params)

def send_video_note(chat_id: str, video_note: str):

    params = {
        'chat_id': chat_id,
        'video_note': video_note
    }

    sendvn_url = f'{BASE_URL}/sendVideoNote'
    requests.get(sendvn_url, params=params)


def send_media_group(chat_id: str, media):

    params = {
        'chat_id': chat_id,
        'media': media
    }    
    sendmg_url = f'{BASE_URL}/sendMediaGroup'
    requests.get(sendmg_url, params)

def send_location(chat_id: str, latitude: float, longitude: float):
    params = {
        'chat_id': chat_id,
        'latitude': latitude,
        'longitude': longitude
    }
    sendlocation_url = f'{BASE_URL}/sendLocation'
    requests.get(sendlocation_url, params=params)


def updater(token: str):

    offset = None

    while True:

        updates = get_updates(offset)

        for update in updates:
            
            if 'message' in update:
                message = update['message']
                user = update['message']['from']

                if 'text' in message:
                    send_message(user['id'], message['text'])    
            
                elif 'contact' in message:
                    contact = message['contact']
                
                    send_contact(user['id'], contact['first_name'], contact['phone_number'])
            
                elif 'photo' in message:
                    photo = message['photo'][0]
                
                    send_photo(user['id'], photo['file_id'])
            
                elif 'document' in message:
                    document = message['document']
                
                    send_document(user['id'], document['file_id'])
                
                elif 'audio' in message:
                    audio = message['audio']

                    send_audio(user['id'], audio['file_id'])

                elif 'voice' in message:
                    voice = message['voice']

                    send_voice(user['id'], voice['file_id'])

                elif 'animation' in message:
                    animation = message['animation']

                    send_animation(user['id'], animation['file_id'])

                elif 'video' in message:
                    video = message['video']

                    send_video(user['id'], video['file_id'])    

                elif 'video_note' in message:
                    video_note = message['video_note']

                    send_video_note(user['id'], video_note['file_id'])

                elif 'media' in message:
                    media = message['media']

                    send_media_group(user['id'], media['file_id'])    
                
                elif 'location' in message:
                    location = message['location']
                    send_location(user['id'], location['latitude'], location['longitude'])

            
            offset = update['update_id'] + 1

        sleep(1)

if __name__ == '__main__':
    updater(token)
