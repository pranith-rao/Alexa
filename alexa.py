import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests,sys
import smtplib
import webbrowser,os
import smtplib
import cv2
from requests import get

alexaa = pyttsx3.init('sapi5')                                                 #text-to-speech converter
voices = alexaa.getProperty('voices')                                          #gets all voices
alexaa.setProperty('voice', voices[1].id)                                      #1 for female voice and 0 for male voice

def talk(text):                                                                #function that makes alexa speak
    alexaa.say(text)                                                           #alexa's replies
    alexaa.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good Morning!")
    elif hour>=12 and hour<18:
        talk("Good Afternoon!")   
    else:
        talk("Good Evening!")  
    talk("I am Alexa How can i help you?")  

def weather(city): 
    api_key = "b698f17eaff024ba14b301514e2f321a"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
    response = requests.get(complete_url) 
    x = response.json() 
    if x["cod"] != "404": 
        y = x["main"] 
        current_temperature = y["temp"] 
        #current_pressure = y["pressure"] 
        #current_humidiy = y["humidity"] 
        #z = x["weather"] 
        #weather_description = z[0]["description"]
        return str(current_temperature)

def take_command():                                                         #function to take commands from users
    listener = sr.Recognizer()                                              #speech recognizer
    with sr.Microphone() as source:                                         #our microphone will be used as source to take commands
        print('Alexa is listening...')                                      #indication that alexa is ready
        listener.pause_threshold = 1
        voice = listener.listen(source,timeout=6,phrase_time_limit=5)       #alexa listens to your command
    try:
        print("Recognizing...")
        command = listener.recognize_google(voice,language='en-in')         #your command is converted into text using google api
        print(f"You said: {command}")
    except Exception as e:
        print("Say that again please")
        return "None"
    return command

def sendEmail(to, content):                                                #function to send a email to someone
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('gtafive5one@gmail.com', 'epicgame1')
    server.sendmail('gtafive5one@gmail.com', to, content)
    server.close()

#setting chrome as the browser to open sites
webbrowser.register('chrome',None,
	webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"))

if __name__ == "__main__":
    wishMe()
    while True:
        command = take_command().lower()
        if 'play' in command:                                               #command to play song
            song = command.replace('play', '')                              #play is removed from command so that we get the song name
            talk('playing ' + song)                                         #alexa will inform us which song is being played
            pywhatkit.playonyt(song)                                        #song will be played on youtube
        elif 'the time' in command:                                         #if time is asked
            time = datetime.datetime.now().strftime('%I:%M %p')             #time is converted into string using strftime() %I is 12-hour clock %M is minutes %p is am or pm
            talk('Current time is ' + time)
        elif 'who is' in command:
            try:
                person = command.split("who is",1)[1]                       #command will be trimmed to only the subject name after who is 
                person = str(person)
                info = wikipedia.summary(person, 1, auto_suggest=False)     #alexa will go through wikipedia and tell us about it. 1 specifies no.of statemets you want about the subject
                print(f"According to Wikipedia: {info}")
                talk(info)
            except:
                talk("Sorry no results found")
        elif 'date' in command:
            date = datetime.date.today().strftime("%B %d, %Y")              #month,day,year
            talk('Todays date is'+ str(date))
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'weather' in command:
            try:
                city = str(command.split("in",1)[1])
                weather_api = weather(city)
                talk('Weather in' +city +'is'+ weather_api + 'degree fahreneit')
            except:
                talk("Sorry I dont know that place")
        elif 'wikipedia' in command:
            talk('Searching Wikipedia..')
            try:
                command = command.replace("wikipedia", "")
                info = wikipedia.summary(command, 1, auto_suggest=False)
                talk("According to wikipedia")
                print(f"According to Wikipedia: {info}")
                talk(info)
            except:
                talk("Sorry no results found")
        elif 'open youtube' in command:
            talk("Opening youtube")
            webbrowser.get('chrome').open("youtube.com")
        elif 'open google' in command:
            talk("What should I search on google?")
            try:
                search = take_command().lower()
            except:
                talk("Please repeat it again")
                search = take_command().lower()
            talk("Fetching your results from google")
            webbrowser.get('chrome').open(f"google.com/search?q={search}")
        elif 'open stackoverflow' in command:
            talk("Opening stackflow")
            webbrowser.get('chrome').open("stackflow.com")
        elif 'open code' in command:
            talk("Opening visual studio code")
            vs_path = "C:\\Users\\prani\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vs_path)
        elif 'open command prompt' in command:
            os.system("start cmd")
        elif "open camera" in command:
            cap = cv2.VideoCapture(0)
            while True:
                ret ,img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        elif "open notepad" in command:
            np_path = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(np_path)
        elif "close notepad" in command:
            talk("Closing notepad")
            os.system("taskkill /f /im notepad.exe")  
        elif "ip address" in command:
            ip = get('https://api.ipify.org').text
            print(f"Your IP address is {ip}")
            talk(f"Your IP address is {ip}")        
        elif 'email to' in command:
            try:
                to = "pranithrao3@gmail.com"
                talk("What should I say?")
                content = take_command()    
                sendEmail(to, content)
                talk("Email has been sent!")
            except Exception as e:
                print(e)
                talk("Sorry! I am not able to send this email")
        elif 'send whatsapp message' in command:
            #(number with country code,message,hours in 24-format,minutes) At the time specified message will be sent
            pywhatkit.sendwhatmsg("+917019821076","message from alexa",22,7)                          
            talk("Message has been sent")   
        elif 'stop' in command:
            talk("Thank you for using me. Goodbye!")
            sys.exit()
        elif 'thank you' in command:
            talk("Thank you for using me. Goodbye!")
            sys.exit()
        elif 'are you single' in command:
            talk("Yes, but to be honest, I don't think so.")
        elif 'do you love me' in command:
            talk("Yes, and only because you’re enjoying it.")
        else:
            talk('Sorry I dont know that')
