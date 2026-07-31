import speech_recognition as sr
import webbrowser
import pyttsx3

reconizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    
    engine.say(text)
    engine.runAndWait()
    


if __name__ == "__main__":
    speak("Hello Krish Sir... I'm you'r personal Assistant... ")
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = reconizer.listen(source)
        try:
            text = reconizer.recognize_google(audio)
            print(f"You said: {text}")
            break 
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            