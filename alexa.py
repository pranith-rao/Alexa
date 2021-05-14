import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests,json,sys

listener = sr.Recognizer()                                      #speech recognizer
alexaa = pyttsx3.init()                                         #text-to-speech converter
voices = alexaa.getProperty('voices')                           #gets all voices
alexaa.setProperty('voice', voices[1].id)                       #1 for female voice and 0 for male voice

def talk(text):                                                 #function that makes alexa speak
    alexaa.say(text)                                            #alexa's replies
    alexaa.runAndWait()

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

def take_command():                                             #function to take commands from users
    try:
        with sr.Microphone() as source:                         #our microphone will be used as source to take commands
            print('Alexa is listening...')                      #indication that alexa is ready
            voice = listener.listen(source,None,10)                     #alexa listens to your command for 10 secs
            command = listener.recognize_google(voice)          #your command is converted into text using google api
            command = command.lower()                           #command is converted to lower case
            if 'alexa' in command:
                command_for_alexa = command.replace('alexa', '')          #alexa is removed from command so that main command can be executed
                print(command)
    except:
        pass
    return command_for_alexa


def run_alexa():
    command = take_command()
    if 'play' in command:                                       #command to play song
        song = command.replace('play', '')                      #play is removed from command so that we get the song name
        talk('playing ' + song)                                 #alexa will inform us which song is being played
        pywhatkit.playonyt(song)                                #song will be played on youtube
    elif 'time' in command:                                     #if time is asked
        time = datetime.datetime.now().strftime('%I:%M %p')     #time is converted into string using strftime() %I is 12-hour clock %M is minutes %p is am or pm
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.split("who is",1)[1]                   #command will be trimmed to only the subject name after who is 
        person = str(person)
        print(person)
        info = wikipedia.summary(person, 1,auto_suggest=False)   #alexa will go through wikipedia and tell us about it. 1 specifies no.of statemets you want about the subject
        talk(info)
    elif 'date' in command:
        date = datetime.date.today().strftime("%B %d, %Y")      #month,day,year
        talk('Todays date is'+ str(date))
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'weather' in command:
        city = command.split("in",1)[1]
        weather_api = weather(city)
        talk('Weather in' +city +'is'+ weather_api + 'degree fahreneit')
    elif 'stop' or 'thank you' in command:
        print(command)
        sys.exit()
    elif 'are you single' or 'do you love me' in command:
        print(command)
        talk('No I am in a relationship with wifi')
    else:
        talk('Please say the command again.')


while True:
    try:
        run_alexa()
    except UnboundLocalError:
        print("No command detected! Alexa has stopped working ")
        break

