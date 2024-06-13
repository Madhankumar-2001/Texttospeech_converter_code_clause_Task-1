from gtts import gTTS

import os

mytext = 'Hi this taks is based on text to speech converter. In this task some text will be given to me and I will give voice for that text.'

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome.mp3")

os.system("start welcome.mp3")

