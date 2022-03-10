import speech_recognition as sr
import Functions as fun


class VoiceHandle:
    def __init__(self):
        self.r = sr.Recognizer()
        self.r.pause_threshold = .4
        self.r.non_speaking_duration = .3
        self.mic = sr.Microphone(device_index=1)
        self.r.energy_threshold = 300


    def StartListening(self):
        try:
            with self.mic as source:
                self.r.adjust_for_ambient_noise(source)
                audio = self.r.listen(source)
                print("yes")

            text = self.r.recognize_google(audio, language="pl-PL",).upper()
            print(text)
            if "KAPI" in text or "CAPRI" in text or "GABI" in text:
                return True
            else:
                return False

        except sr.UnknownValueError:
            return False



    def ListenToCommands(self):
        self.r.energy_threshold = 0
        try:
            with self.mic as source:
                self.r.adjust_for_ambient_noise(source)
                audio = self.r.listen(source)
            text = self.r.recognize_google(audio, language="pl-PL").upper()

            print(text)


            if("ZAKOŃCZ" in text):
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
            commandList = {
                "STOP":fun.StopStart,
                "DATA":fun.Date,
                "GODZINA":fun.Time
            }
            commandList[command]()
            return True
        except KeyError:
            return False

#sd

