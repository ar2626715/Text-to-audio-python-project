from gtts import gTTS
#pip install gtts
from playsound import playsound
#pip install playsound

audio = 'speech.mp3'
language = 'en'

sp = gTTS(text="My name is Abhinav raj", lang=language,slow=False)

sp.save(audio)
playsound(audio)


