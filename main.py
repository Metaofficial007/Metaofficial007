from gtts import gTTS
from audioplayer import AudioPlayer
import nltk
import speech_recognition as sr
import functions
from flask import Flask, render_template, Response, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html');

def main():
    global task

    recognize = sr.Recognizer()
    with sr.Microphone() as source:
        audio_data = recognize.record(source, duration=5)

        try:
            text = recognize.recognize_google(audio_data)
            task += text
            tasktok = nltk.word_tokenize(task)

            if "YouTube" in tasktok:   #works like a charm
                functions.youtube()
                task = ''