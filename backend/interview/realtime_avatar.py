import cv2
import pyttsx3 
import sounddevice as sd
from scipy.io.wavfile import write
import time

engine = pyttsx3.init()

QUESTIONS = [
    "Tell me about yourself",
    "Explain one project you worked on",
    "What are your strengths"
]

def speak(text):
    engine.say(text)
    engine.runAndWait()

def record_audio(filename="answer.wav", duration=10, fs=44100):
    print("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, audio)
    print("Recording finished")

def start_avatar_interview():
    cap = cv2.VideoCapture(0)

    for q in QUESTIONS:
        speak(q)
        time.sleep(1)
        record_audio()

        ret, frame = cap.read()
        if ret:
            cv2.imshow("AI Avatar Interview (Camera ON)", frame)
            cv2.waitKey(1000)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_avatar_interview()
