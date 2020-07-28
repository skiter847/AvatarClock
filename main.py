from telethon.sync import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
import os
from util import current_time
from image import create_image

API_ID = os.environ.get('api_id')
API_HASH = os.environ.get('api_hash')
SESSION_FILE = os.environ.get('session_file')


def main():
    previous_time = ''
    with TelegramClient(SESSION_FILE, API_ID, API_HASH) as client:
        while True:
            if not previous_time == current_time():
                previous_time = current_time()
                create_image(current_time())
                image = client.upload_file('clock.png')
                client(DeletePhotosRequest(client.get_profile_photos('me')))
                client(UploadProfilePhotoRequest(image))

if __name__ == '__main__':
    main()

