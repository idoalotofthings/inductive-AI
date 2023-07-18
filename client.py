import requests
import speech_recognition as sr
import os

class ClientApp:

    def __init__(self):
        self.recognizer = sr.Recognizer()

    def speech_to_text(self):
        with sr.Microphone() as mic:
            print("speak now!")
            self.recognizer.adjust_for_ambient_noise(mic)
            audio = self.recognizer.listen(mic)    
        try:
            print("Gotcha")
            text = self.recognizer.recognize_google(audio)
            print(text)
            return text
        except:
            return "Say I couldn't get you, please say again"
        
    def speak(self,message):
        os.system(f'espeak "{message}"')
        
app = ClientApp()

speaker_enabled = True


if speaker_enabled:
    
    data = requests.post("https://f3ae-2401-4900-1c22-5ada-b2cf-a652-7597-37dc.ngrok-free.app/ai", f'{{"question":"{app.speech_to_text()}"}}')
    
    app.speak(data.text)