import requests
import os
from mpyg321.mpyg321 import MPyg321Player
from mpyg321 import *
import speech_recognition as sr     # import the library
import subprocess
from gtts import gTTS
from translate import Translator
from playsound import playsound
def main():
    bot_message=""
    message=""
    while bot_message != "Bye" or bot_message!='thanks':
        r= sr.Recognizer()
        mic=sr.Microphone(device_index=1)
        with mic as source:
            # print("Speak Anything:")
            audio= r.listen(source)
            try:
                message= r.recognize_google(audio)
                # print("You said : {}".format(message))
            except:
                print("Sorry could not recognize your voice")
        if len(message)==0:
            continue
        # print("Sending message now...")
        r= requests.post('http://localhost:5005/webhooks/rest/webhook', json={"message":message})
        # print("Bot says, ",end='')
        for i in r.json():
            bot_message=i['text']
            # print(f"{bot_message}")
        myobj = gTTS(text = bot_message)
        myobj.save("welcome.mp3")
        # print('saved')
        # os.system("start welcome.mp3")
        playsound("welcome.mp3")
        os.remove("welcome.mp3")
        main()
main()
