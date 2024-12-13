from dotenv import load_dotenv
import requests
import subprocess
import random
import threading
import sys
import os
from queue import Queue

# Load environment variables from .env file
load_dotenv()

# Fetch credentials from environment variables
API_KEY = os.getenv('API_KEY')

print("API Key:", API_KEY)

url = 'https://api.elevenlabs.io/v1/text-to-speech/t3lBbQWt44zxzcyZcuHc/stream'
headers = {
    'accept': '*/*',
    'xi-api-key': API_KEY,
    'Content-Type': 'application/json'
}

graphemes = ['a', 'e', 'i', 'o', 'u', 't', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'm', 'f', 'p', 'g', 'w', 'y', 'b', 'v', 'k', 'x', 'j', 'q', 'z', 'th', 'er', 'ing', 'the', 'and', 'ion', 'ent', 'at', 'for', 'her', 'en', 'was', 'ere', 'his', 'st', 'ing', 'of', 'to', 'with', 'he', 'in', 'that', 'it', 'as', 'on', 'is', 'ed', 'ar', 'or', 'nt', 'ea', 'ti', 'es', 'ng', 'al', 'de', 'se', 'le', 'sa', 'si', 'an', 'me', 'be', 'ro', 're', 've', 'ur', 'el', 'te', 'co', 'ri', 'ra', 'ic', 'ne', 'la', 'li', 'ho', 'no', 'ra', 'ri', 'so', 'ac', 'ly', 'ma', 'ec', 'us', 'ad', 'ns', 'pe', 'mi', 'ee', 'oo', 'oo', 'lo', 'ce', 'ss', 'da', 'un', 'rs', 'ot', 'ee', 'io', 'pr', 'mo', 'ca', 'ee', 'it', 'ie', 'oo', 'ta', 'fo', 'da', 'wh', 'ev', 'ch', 'wi', 'ba', 'il', 'sh', 'da', 'uc', 'id', 'ow', 'ee', 'il', 'tr', 'am', 'si', 'wa', 'by', 'ow', 'lo', 'ge', 'ho', 'jo', 'sc', 'ag', 'ap', 'go', 'pa', 'up', 'bu', 'fu', 'gu', 'jo', 'mu', 'nu', 'su', 'tu', 'co', 'do', 'ho', 'bu', 'cu', 'fe', 'ga', 'hu', 'lu', 'nu', 'pu', 'ru', 'tu', 'wa', 'bu', 'cu', 'du', 'gr', 'ho', 'ju', 'ka', 'lo', 'ma', 'na', 'pu', 'qu', 'ru', 'su', 'ta', 'vu', 'wa', 'ye', 'zu']

sounds = ['!', 'x', 'q', 'r', 'rr', 's', 'sh', 'f', 'v', 'h', 'z', 'zh', 'h', 'u', 'm', 'n', 'ng', 'l', 'w', 'y', 'oo']

similarity_boost = 0.95
stability = 0.05
set_sound = 0.90

def play_audio(audio_queue):
    while True:
        length = random.randint(8, 50)
        s = ''
        for j in range(length):
            if random.random() < set_sound and len(sounds) > 0:
                s += random.choice(sounds)
            else:
                s += random.choice(graphemes)

        print(s)
        
        data = {
            'text': s,
            'voice_settings': {
                'stability': stability,
                'similarity_boost': similarity_boost
            }
        }

        response = requests.post(url, headers=headers, json=data, stream=True)
        response.raise_for_status()

        for chunk in response.iter_content(chunk_size=4096):
            audio_queue.put(chunk)

def play_audio_from_queue(audio_queue):
    # Create a subprocess to pipe the audio data to ffplay and play it
    ffplay_cmd = ['ffplay', '-autoexit', '-nodisp', '-i', 'pipe:0']
    ffplay_proc = subprocess.Popen(ffplay_cmd, stdin=subprocess.PIPE)

    while True:
        chunk = audio_queue.get()
        ffplay_proc.stdin.write(chunk)
        ffplay_proc.stdin.flush()

def optimize_audio_playback():
    audio_queue = Queue()

    audio_thread = threading.Thread(target=play_audio, args=(audio_queue,))
    audio_thread.daemon = True
    audio_thread.start()

    play_audio_from_queue(audio_queue)

optimize_audio_playback()
