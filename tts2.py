import json
import requests
import pygame

class TextToSpeechService:
    def __init__(self):
        config = json.load(open("config.json"))
        self.url = "https://play.ht/api/v2/tts"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {config['play_ht_api_key']}"
        }

    def speak(self, text):
        data = {
            "speed": 1,
            "text": text,
            "voice": "s3://voice-cloning-zero-shot/cd1e0cf3-0106-4dd2-9406-6ccea4d70cf2/kitt-voice/manifest.json"
        }
        response = requests.post(self.url, headers=self.headers, data=json.dumps(data))
        with open('output.mp3', 'wb') as f:
            f.write(response.content)
        pygame.mixer.init()
        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass