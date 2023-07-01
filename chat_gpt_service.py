import json
from input_listener import InputListener
import struct
import os
import openai
import time
from prompt import prompt_template


config = json.load(open("config.json"))
openai.api_key = config["openai_key"]
if "openai_org" in config:
    openai.organization = config["openai_org"]


class ChatGPTService:
    def __init__(self, prompt=prompt_template):
        self.history = [{"role": "system", "content": prompt}]

    def send_to_chat_gpt(self, message):
        self.history.append({"role": "user", "content": message})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k", messages=self.history
        )
        self.history.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})
        return str.strip(response["choices"][0]["message"]["content"])
