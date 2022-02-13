import speech_recognition as sr
import Functions as fun

class VoiceHandle:
    def __init__(self):
        self.r = sr.Recognizer()
        self.r.pause_threshold = .4
        self.r.non_speaking_duration = 0
        self.mic = sr.Microphone(device_index=1)


    def StartListening(self):
        try:
            with self.mic as source:
                self.r.adjust_for_ambient_noise(source)
                audio = self.r.listen(source)

            text = self.r.recognize_google(audio, language="pl-PL").upper()
            print(text)

            if (text[:2] == "KA" or text[:2] == "CA"):
                return True
            else:
                return False

        except sr.UnknownValueError:
            return False



    def ListenToCommands(self):
        try:
            with self.mic as source:
                self.r.adjust_for_ambient_noise(source)
                audio = self.r.listen(source)
            text = self.r.recognize_google(audio, language="pl-PL").upper()

            print(text)


            if(text == "ZAKOŃCZ"):
                print("Bye Bye")
                return False

            finished = self.Commands(text)
            if(not finished):
                print("Nie znam tej komendy")
            elif(finished):
                return False


            return True

        except sr.UnknownValueError:
            return True

    def Commands(self, command):
        try:
            commandList = {"STOP":fun.StopStart}
            commandList[command]()
            return True
        except KeyError:
            return False

