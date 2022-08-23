
from gtts import gTTS
from playsound import playsound

audio = 'audio.mp3'
language = 'pt'

sp = gTTS( text='Testando o texto para som', lang=language, tld='com.br')

sp.save(audio)
playsound(audio)

