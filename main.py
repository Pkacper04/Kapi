from threading import Thread
import VoiceHandeler
import Functions as fun




listening = False

Voice = VoiceHandeler.VoiceHandle()

while(1):
    if(not listening and Voice.StartListening()):
        Thread(target=fun.Talk,args=("słucham",)).start()
        print("slucham")
        listening = True;
    if(listening):
        listening = Voice.ListenToCommands()



