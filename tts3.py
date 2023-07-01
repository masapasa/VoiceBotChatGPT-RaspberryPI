#%%
import os
import pygame
import requests
import json

url = "https://play.ht/api/v2/tts"

payload = json.dumps({
  "speed": 1,
  "text": "This is our response",
  "voice": "s3://voice-cloning-zero-shot/cd1e0cf3-0106-4dd2-9406-6ccea4d70cf2/kitt-voice/manifest.json"
})
headers = {
  'Content-Type': 'application/json',
  'accept': 'text/event-stream',
  'X-USER-ID': 'YVMb6FW4ixZeRvWK9wejDiVErR43',
  'Location': '/api/v2/tts/s3://voice-cloning-zero-shot/cd1e0cf3-0106-4dd2-9406-6ccea4d70cf2/kitt-voice/manifest.json',
  'Authorization': 'Bearer 07b28c958ac74f41812f57345488f96a'
}

response = requests.request("POST", url, headers=headers, data=payload)
response = response.text
print(response)
print(type(response))
#%%

# with open('output.mp3', 'wb') as f:
#     f.write(response.content)
# pygame.mixer.init()
# pygame.mixer.music.load("output.mp3")
# pygame.mixer.music.play()
# while pygame.mixer.music.get_busy():
#     pass
# os.remove("output.mp3")