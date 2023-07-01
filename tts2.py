#%%
import json
import os
import requests
import pygame

class TextToSpeechService:
    def __init__(self):
        config = json.load(open("config.json"))
        self.url = "https://play.ht/api/v2/tts"
        self.headers = {
            "Content-Type": "application/json",
            "accept": "text/event-stream",
            "Location": "/api/v2/tts/s3://voice-cloning-zero-shot/cd1e0cf3-0106-4dd2-9406-6ccea4d70cf2/kitt-voice/manifest.json",
            "X-USER-ID": config["play_ht_user_id"],
            "Authorization": f"Bearer {config['play_ht_api_key']}"
        }

    def speak(self, text):
        data = {
            "speed": 1,
            "text": "what is your name?",
            "voice": "s3://voice-cloning-zero-shot/cd1e0cf3-0106-4dd2-9406-6ccea4d70cf2/kitt-voice/manifest.json"
        }
        print(self.headers)
        print(self.url)
        response = requests.post(url=self.url, headers=self.headers, json=data)
        response_data = response.json()
        web = response_data['url']
        print(web)
        print(response_data)

        print(response.json())
        print(response.status_code)
        print(f"post_url", response.url)
        with open('output.mp3', 'wb') as f:
            f.write(response.content)
        # pygame.mixer.init()
        # pygame.mixer.music.load("output.mp3")
        # pygame.mixer.music.play()
        # while pygame.mixer.music.get_busy():
        #     pass
        # os.remove("output.mp3")
#%%
import pycurl
import json
from io import BytesIO

buffer = BytesIO()
data = {
    "speed": 1,
    "text": "This is our response",
    "voice": "s3://voice-cloning-zero-shot/cd1e0cf3-0106-4dd2-9406-6ccea4d70cf2/kitt-voice/manifest.json"
}

c = pycurl.Curl()
c.setopt(c.URL, 'https://play.ht/api/v2/tts')
c.setopt(c.WRITEDATA, buffer)
c.setopt(c.HTTPHEADER, ['Content-Type: application/json', 'accept: text/event-stream', 
                        'X-USER-ID: YVMb6FW4ixZeRvWK9wejDiVErR43', 'Location: /api/v2/tts/s3://voice-cloning-zero-shot/cd1e0cf3-0106-4dd2-9406-6ccea4d70cf2/kitt-voice/manifest.json',
                        'Authorization: Bearer 07b28c958ac74f41812f57345488f96a'])
c.setopt(c.POSTFIELDS, json.dumps(data))
c.perform()
c.close()

body = buffer.getvalue()
print('Output: ', body.decode('utf-8'))
# %%
import requests
import json
url = "https://play.ht/api/v2/tts"
headers = {
    "Content-Type": "application/json",
    "accept": "text/event-stream",
    "Location": "/api/v2/tts/s3://voice-cloning-zero-shot/cd1e0cf3-0106-4dd2-9406-6ccea4d70cf2/kitt-voice/manifest.json",
    "X-USER-ID": "YVMb6FW4ixZeRvWK9wejDiVErR43",
    "Authorization": "Bearer 07b28c958ac74f41812f57345488f96a"
}
data = {
    "speed": 1,
    "text": "what is your name?",
    "voice": "s3://voice-cloning-zero-shot/cd1e0cf3-0106-4dd2-9406-6ccea4d70cf2/kitt-voice/manifest.json"
}
response = requests.post(url, headers=headers, json=data)
print("+++++++++++++++++++++++")
print(response)
response_data = response.json()
web = response_data['url']
print(web)
print(response_data)
print("+++++++++++++++++++++++")

print(response)
print(response.status_code)
print(response.url)
with open('output.mp3', 'wb') as f:
    f.write(response.content)
# %%
