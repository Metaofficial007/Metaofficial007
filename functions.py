from gtts import gTTS
from audioplayer import AudioPlayer
from googlesearch import search
import speech_recognition as sr
import nltk
import webbrowser








def youtube():           #works

    mytext = "Opening youtube"
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("speech.mp3")
    AudioPlayer("speech.mp3").play(block=True)

    webbrowser.open_new("https://www.youtube.com/")


youtube()