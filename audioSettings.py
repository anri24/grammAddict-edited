import pyttsx3
from GramAddict.core.config import Config
import yaml

crash_audio_warning = True

engine = pyttsx3.init()
def talk(text):
    if (crash_audio_warning == True):
        engine.setProperty('rate',150)
        voice = engine.getProperty('voices')
        engine.setProperty('voice', voice[1].id)
        engine.say(text)
        engine.runAndWait()