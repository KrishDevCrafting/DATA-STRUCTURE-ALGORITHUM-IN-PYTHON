import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLibrary

recognizer = sr.Recognizer()

def ProcessCommand(c):
    c_lower = c.lower()
    if "open google" in c_lower:
        speak("Opening Google Sir")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c_lower:
        speak("Opening YouTube Sir")
        webbrowser.open("https://www.youtube.com")
    elif "open github" in c_lower:
        speak("Opening GitHub Sir")
        webbrowser.open("https://www.github.com")
    elif "play" in c_lower or any(song in c_lower for song in musicLibrary.music):
        # 1. First check if any song from our music library is mentioned
        found_song = None
        for song in musicLibrary.music:
            if song in c_lower or song.replace(" ", "") in c_lower.replace(" ", ""):
                found_song = song
                break
        
        if found_song:
            speak(f"Playing {found_song} Sir")
            webbrowser.open(musicLibrary.music[found_song])
        else:
            # 2. If it's a song not in our dictionary, search & play on YouTube!
            search_term = c_lower.replace("play", "").replace("song", "").strip()
            if search_term:
                speak(f"Playing {search_term} on YouTube Sir")
                webbrowser.open(f"https://www.youtube.com/results?search_query={search_term}")
            else:
                speak("Which song would you like to play Sir?")
    else:
        speak("I am not sure how to handle that command yet.")

 

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
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)
                print("Recognizing...")
                
                text = recognizer.recognize_google(audio)
                print(f"You said: {text}")
                
                if "jarvis" in text.lower():
                    # Check if command was already spoken in the same sentence (e.g. "Jarvis open Google")
                    command_part = text.lower().replace("jarvis", "").strip()
                    if command_part:
                        ProcessCommand(command_part)
                    else:
                        # Two-step mode: User only said "Jarvis"
                        speak("Yes Sir, How can I help you?")
                        print("Jarvis listening for your command...")
                        audio = recognizer.listen(source, timeout=4, phrase_time_limit=5)
                        command = recognizer.recognize_google(audio)
                        print(f"Command: {command}")
                        ProcessCommand(command)
                
            except sr.WaitTimeoutError:
                # Catches silence without crashing the program
                print("No speech detected within the timeout period. Listening again...")
            except sr.UnknownValueError:
                print("Could not understand audio.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")