import os
from bot1 import spammingBot

# Use a path relative to this file so it works regardless of folder name
base_dir = os.path.dirname(os.path.abspath(__file__))
txt_path = os.path.join(base_dir, 'text.txt')

with open(txt_path, 'r') as txt:
    content = txt.read()
    for word in content.split():
        print(f"Sending: {word}")
        spammingBot(word
