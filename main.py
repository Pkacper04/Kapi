from threading import Thread
import playsound
import VoiceHandeler




listening = False

Voice = VoiceHandeler.VoiceHandle()

while(1):
    if(not listening and Voice.StartListening()):
        Thread(target = playsound.playsound, args = ("AudioSources\slucham.mp3",)).start()
        print("slucham")
        listening = True;
    if(listening):
        listening = Voice.ListenToCommands()



