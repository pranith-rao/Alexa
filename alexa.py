from typing import Text
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests,sys,json
import smtplib
import webbrowser,os
import smtplib,time,PyPDF2
import cv2
from requests import get
import pyautogui
import instaloader
import self_tweet

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
        print("Sorry I dont know that")
        return "None"
    return command

def sendEmail(to, content):                                                #function to send a email to someone
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('gtafive5one@gmail.com', 'epicgame1')
    server.sendmail('gtafive5one@gmail.com', to, content)
    server.close()

def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=b4949ddb6afd4593a1176f76bfe0a288'
    fetched_news = requests.get(main_url).json()
    articles = fetched_news['articles']
    headlines = []
    day = ["first","second","third","fourth","fifth"]
    for ar in articles:
        headlines.append(ar["title"])
    for i in range(len(day)):
        print(f"Today's {day[i]} news is: {headlines[i]}")
        talk(f"Today's {day[i]} news is: {headlines[i]}")

def mylocation():
    try:
        ip_address = requests.get('https://api.ipify.org').text
        url = 'https://get.geojs.io/v1/ip/geo/'+ip_address+'.json'
        geo_requests = requests.get(url)
        geo_data = geo_requests.json()
        city = geo_data['city']
        country = geo_data['country']
        talk(f"I am not sure, but I think we are in {city} city of {country} country")
    except Exception as e:
        talk("Sorry, but due to network issues I am not able to track our location")
        pass

def insta():
    talk("Please enter the correct user name")
    name = input("Enter insta ID here:")
    talk(f"Here is the innsta gram profile of {name}")
    webbrowser.open(f"www.instagram.com/{name}")
    time.sleep(3)
    talk("Would you like to download the profile picture of this account?")
    reply = take_command().lower()
    if "yes" in reply:
        instagram = instaloader.Instaloader()
        instagram.download_profile(name, profile_pic_only = True)
        talk("Done, profile picture has been saved")
    else:
        talk("OK")
        pass

def pdf_reader():
    pdf = open('The_Night_We_Met.pdf','rb')                                   #read binary
    pdfReader = PyPDF2.PdfFileReader(pdf)
    pages = pdfReader.numPages
    talk(f'Total number of pages in this pdf is {pages}')
    talk('Please enter the page number you want me to read')
    page_no = int(input("Enter the page number here: "))
    page_no = page_no - 1
    page = pdfReader.getPage(page_no)
    content = page.extractText()

    #to increase speech-speed
    time.sleep(1)
    talk('Please enter the number of words i have to read per minute')
    time.sleep(1)
    voiceRate = int(input("Enter the number of words to be read per minute(default is 200): "))
    time.sleep(1)
    alexaa.setProperty('rate',voiceRate)
    talk(content)
    alexaa.setProperty('rate',200)
    time.sleep(2)

    talk('Done, page finished')

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
        elif 'stop' in command or 'thank you' in command:
            talk("Thank you for using me. Goodbye!")
            sys.exit()
        elif 'are you single' in command:
            talk("Yes, but to be honest, I don't think so.")
        elif 'do you love me' in command:
            talk("Yes, and only because you’re enjoying it.")
        elif 'switch the window' in command:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        elif "news" in command:
            talk("Fetching today's latest news")
            news()
        elif "shut down the system" in command:
            talk("Shutting down")
            os.system("shutdown /s /t 5")
        elif "restart the system" in command:
            talk("Restarting")
            os.system("shutdown /r /t 5")
        elif "the system into sleep" in command:
            talk("Sleep mode ON")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        elif "where am I" in command or "what is my location" in command or "where are we" in command:
            talk("Let me check")
            mylocation()
        elif "instagram profile" in command or "profile on instagram" in command:
            insta()
        elif "take a screenshot" in command or  "screenshot the screen" in command:
            talk("In what name the screenshot must be saved?")
            name = take_command().lower()
            talk("Leave the screen idle for 3 seconds")
            time.sleep(3)
            screenshot = pyautogui.screenshot()
            screenshot.save(f"{name}.png")
            talk("Done, screenshot is captured")
        elif "tweet" in command:
            #have your twitter cerdentials saved in twitter_info.txt file
            talk("What you want to tweet?")
            tweet = take_command().capitalize()
            if tweet == 'none':
                talk("tweet can't be empty")
                continue
            else:
                try:
                    self_tweet.tweet(tweet)
                    talk("Done, Tweeted successfully!")
                except:
                    talk("Tweet failed")
                    pass
        elif "pdf" in command:
            pdf_reader()
        elif "hide all files" in command or "hide this folder" in command:  
            os.system("attrib +h /s /d")
            talk("All the files in the current directory are hidden")
        elif "visible to everyone" in command:
            talk("Are you sure?")
            reply = take_command().lower()
            if "yes" in reply:
                os.system("attrib -h /s /d")
                talk("All the files in the current directory are visible to everyone now")
            else:
                talk("Ok, Files untouched")
        else:
            talk('Sorry I dont know that')
