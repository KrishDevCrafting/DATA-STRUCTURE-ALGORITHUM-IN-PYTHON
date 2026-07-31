import speech_recognition as sr
import pyttsx3
import webbrowser

recognizer = sr.Recognizer()

def ProcessCommand(C):
    if "open google" in C.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in C.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open github" in C.lower():
        webbrowser.open("https://www.github.com")


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello Krish Sir... I'm your personal assistant jarvis...")
    
    # Keep the microphone object initialized outside or inside the loop cleanly
    with sr.Microphone() as source:
        # Adjust for ambient background noise once at startup
        print("Adjusting for background noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        while True:
            print("\nListening...")
            try:
                # Increased timeout to give you more time to start talking
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=5)
                print("Recognizing...")
                
                text = recognizer.recognize_google(audio)
                if "jarvis" in text.lower():
                    speak("Yes Sir, How can I help you?")
                    # Listen for the next command after acknowledging
                    print("Jarvis listening for your command...")
                    audio = recognizer.listen(source, timeout=2, phrase_time_limit=5)
                    command = recognizer.recognize_google(audio)
                    print(f"You said: {command}")
                    ProcessCommand(command)
                print(f"You said: {text}")
                
            except sr.WaitTimeoutError:
                # Catches silence without crashing the program
                print("No speech detected within the timeout period. Listening again...")
            except sr.UnknownValueError:
                print("Could not understand audio.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")