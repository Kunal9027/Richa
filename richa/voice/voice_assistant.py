
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os

#------INITIALIZING MODULES & FUNCTIONS------#

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):      
    engine.say(text)
    engine.runAndWait()

def listen():         
    with sr.Microphone() as source:
        print("Assistant : Listening...")
        recognizer.adjust_for_ambient_noise(source )
        audio = recognizer.listen(source)
        print("Assistant : Recognizing...")      
        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            speak("Sorry, could not understand audio.")
            print("Sorry, could not understand audio.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results: {e}")
            return ""


def wishMe():         
    
    hour = int(datetime.datetime.now().hour)
    if hour>= 6 and hour<12:
        speak("Good Morning !")
  
    elif hour>= 12 and hour<16:
        speak("Good Afternoon !")   
  
    else:
        speak("Good Evening !")

def main():   
   
    wishMe()
    speak("I am Richa's voice assistant. Please tell me how can I help you")
  
    while True:
                
        command = listen().lower() # it takes microphone input from the user and returns string output in lower case        

        if {"hello", "hi", "hey"} & set(command.split()):
            speak("Hello what can i do for you")
        
        elif 'how are you' in command:
            speak("I am fine, Thank you sir")
            speak("How are you, Sir")
        
            if 'fine' in command or "good" in command:
                speak("It's good to know that your fine")
            
        
        
        
        elif {"time", "date"} & set(command.split()):
            now = datetime.datetime.now()
            speak("Current date and time : ")
            speak(now.strftime("%d-%m-%Y %H:%M:%S"))
            print(now.strftime("%d-%m-%Y %H:%M:%S"))
        
        elif "google search" in command or "search on google" in command:
             while True:          
                speak("what should i search on google")
                query = listen()
                if query:
                    search_url = f"https://www.google.com/search?q={query}"
                    webbrowser.open(search_url)
                    speak(f"Here are the search results for '{query}'.")
                    break               
                
            
        elif "open brave" in command:
            speak("opening brave")
            os.startfile("C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe")
          
        elif "close brave" in command:
            speak("closing brave")
            os.system("taskkill /f /im brave.exe")    
                
        elif 'open youtube' in command:             # it open youtube
            speak("opening youtube")
            search_url = f"https://www.youtube.com/"
            webbrowser.open(search_url)

        elif 'search on youtube' in command:        # it search on youtube
             while True:
                speak("what should i search on youtube")
                query = listen()
                if query:
                    search_url = f"https://www.youtube.com/results?search_query={query}"
                    webbrowser.open(search_url)
                    speak(f"Here are the search results for '{query}'.")
                    break 
 
        elif 'open google' in command:              # it open google
            speak("opening google")
            search_url = f"https://www.google.com/"
            webbrowser.open(search_url)
            
        elif 'open stackoverflow' in command:         # it open stackoverflow
            speak("Here you go to Stack Over flow. Happy coding")
            search_url = f"https://www.stackoverflow.com/"
            webbrowser.open(search_url)  
                    
        elif "wikipedia" in command:
            speak("Here you go to wikipedia")
            search_url = f"https://www.wikipedia.com/"
            webbrowser.open(search_url)      
        
          
        elif "open notepad" in command:
            speak("opening notepad")
            os.startfile("C:\\Windows\\System32\\notepad.exe")    
      
            
        elif "close notepad" in command:
            speak("closing notepad")
            os.system("taskkill /f /im notepad.exe")
            
       
 
        elif "wish me" in command:
            wishMe()
               
                
        elif {"about" , "who", "tell me about yourself"} & set(command.split()):
          #  print("I am a voice assistant created by the greatest enginner of all time. The one and only my mastre Kunal Chaudhary")
            speak("I am a voice assistant created by the greatest enginner of all time. The one and only my mastre Richa Chaudhary")
        
        elif {"exit", "stop", "quit"} & set(command.split()):
            speak("Goodbye!")
            break
       
        
if __name__ == "__main__":
    main()