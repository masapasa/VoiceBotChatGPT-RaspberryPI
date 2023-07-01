import json
import struct
import os
import time
import boto3
import pygame

class TextToSpeechService:
    def __init__(self):
        config = json.load(open("config.json"))

        self.polly = boto3.client('polly',
                                    aws_access_key_id=config["aws_access_key_id"],
                                    aws_secret_access_key=config["aws_secret_access_key"],
                                    region_name=config["aws_region"])

    def speak(self, text):
        response = self.polly.synthesize_speech(VoiceId='Matthew',
                                                OutputFormat='mp3',
                                                Text=text)
        with open('output.mp3', 'wb') as f:
            f.write(response['AudioStream'].read())
        pygame.mixer.init()     
        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass

        os.remove("output.mp3")