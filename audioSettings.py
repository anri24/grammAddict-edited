import pyttsx3


audio = 1

engine = pyttsx3.init()

def talk(text):
    engine.setProperty('rate',150)
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[1].id)
    engine.say(text)
    engine.runAndWait()