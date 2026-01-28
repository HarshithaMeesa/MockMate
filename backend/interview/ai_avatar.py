import pyttsx3
import sounddevice as sd
from scipy.io.wavfile import write

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def ask_and_record(question, filename):
    speak(question)

    fs = 44100
    seconds = 8

    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()

    write(filename, fs, recording)
