from gtts import gTTS
import os
file = open("hi.txt", "r").read()
speech = gTTS(text=file, lang='en', slow = False)
speech.save("voice.mp3")
os.system("voice.mp3")
print(file)