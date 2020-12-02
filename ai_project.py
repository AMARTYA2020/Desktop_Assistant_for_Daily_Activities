import pyttsx3 
import speech_recognition as speech_recognition
import datetime
import wikipedia 
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am your Desktop assistant Please command me ")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening your voice sir.....................")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Sir trying to Recognize input voice....... ...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        
        print("Could you please repeat again...............")  
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia....................................')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

                   #CHANGE THE DRIVE AND LOCATION ACCORDING TO WHERE YOU HAVE STORED SONGS 
        elif 'play music' in query:
            music_dir = 'D:\\favourite songs\\songs\\herb_alpert'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
            

            


        

        


