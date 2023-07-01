import json
import os
import requests
import pygame

class TextToSpeechService:
    def __init__(self):
<<<<<<< Updated upstream
        #load AWS credentials from config file
        config = json.load(open("config.json"))
        #use polly boto3 client with the crednetials

        self.polly = boto3.client('polly',
                                    aws_access_key_id=config["aws_access_key_id"],
                                    aws_secret_access_key=config["aws_secret_access_key"],
                                    region_name=config["aws_region"])
=======
        pass
>>>>>>> Stashed changes

        #self.polly = boto3.client('polly')


    def speak(self, text):
<<<<<<< Updated upstream
        response = self.polly.synthesize_speech(VoiceId='Matthew',
                                                OutputFormat='mp3',
                                                Text=text)
        with open('output.mp3', 'wb') as f:
            f.write(response['AudioStream'].read())
        
        #play using pygame
        pygame.mixer.init()     
        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass

        os.remove("output.mp3")

=======
        
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
            "text": text,
            "voice": "s3://voice-cloning-zero-shot/cd1e0cf3-0106-4dd2-9406-6ccea4d70cf2/kitt-voice/manifest.json"
        }
        response = requests.request("POST", url, headers=headers, json=data)
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
        # pygame.mixer.init()
        # pygame.mixer.music.load("output.mp3")
        # pygame.mixer.music.play()
        # while pygame.mixer.music.get_busy():
        #     pass
        # os.remove("output.mp3")
>>>>>>> Stashed changes
