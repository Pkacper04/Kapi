import keyboard
import playsound
from gtts import gTTS
import os
from threading import Thread
import datetime

def Talk(speak):
    myobj = gTTS(text=speak, lang="pl", slow=False)
    myobj.save("AudioSources/slucham.mp3")
    playsound.playsound("AudioSources/slucham.mp3")
    os.remove("AudioSources/slucham.mp3")


def StopStart():
    Thread(target=Talk, args=("Zatrzymałem dla ciebie film", )).start()
    keyboard.press("space")

def Date():
    data = datetime.date.today()
    speach = "Dzisiaj jest rok "+str(data.year) + "  miesiac "+str(data.month)+ "  dzień: "+str(data.day)
    Thread(target=Talk, args=(speach,)).start()

def Time():
    now = datetime.datetime.now()
    current_time = "Jest godzina: "+ now.strftime("%H:%M:%S")
    Thread(target=Talk, args=(current_time,)).start()