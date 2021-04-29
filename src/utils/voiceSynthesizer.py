import pyttsx3

class VoiceSynthesizer:
    egine = None
    def __init__(self, engine=None, voice=1, volume=1.0, rate=200):
        self.engine = pyttsx3.init()
        self.setVoice(voice)
        self.setVolume(volume)
        self.setRate(rate)

    def setVoice(self, genderBinary):
        voices = self.engine.getProperty('voices')
        if(genderBinary == 0 or genderBinary == 1):
            self.engine.setProperty('voice', voices[genderBinary].id)
        

    def setVolume(self, decimalVolume):
        self.engine.setProperty('volume', 1.0) 

    def setRate(self, rate):
        self.engine.setProperty('rate', rate)

    def readText(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
        self.engine.stop()