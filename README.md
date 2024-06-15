# Desktop Assistent: Alexa
This non-AI desktop assistant, named Alexa, is built using Python and leverages the SAPI5 text-to-speech engine for vocal responses. Various Python modules are utilized to perform a wide range of tasks, making Alexa a versatile and useful tool for day-to-day activities.  

Presented this project at **Hack the Mountains 2.0** hackathon and placed in the top 55 teams amongst 300+ teams.

## Features
1. Graphical User Interface (GUI):  
   - A user-friendly interface with 'Run' and 'Exit' buttons.  
   - Clicking 'Run' initiates Alexa, while 'Exit' shuts down the application.  

2. Voice Activation and Command Execution:
   - Alexa starts in a sleep mode for minimal disruption.
   - Activate Alexa by saying "ALEXA WAKE UP".
   - Wait for "Alexa is listening..." to be printed on the terminal before issuing any commands.

3. Speech Recognition:
   - Alexa uses Google’s API to convert spoken commands into text.
   - The recognized text is converted to lowercase to ensure consistent command matching.

4. Command Handling:
   - Alexa listens for specific commands and executes predefined tasks if present in the IF-ELSE ladder.
   - If an unknown command is issued, Alexa responds with "Sorry, I don't know that".

5. Sleep and Shutdown Commands:
   - Say "sleep" to put Alexa back into sleep mode.
   - Say "stop" to shut down Alexa.

## Getting Started
1. Clone this repo into your local machine and open it using VS code or any other editor of your choice.
2. Open the terminal and create a virtual environment using the command "python -m venv yourenvname".
3. Activate the virtual env created using the command "yourenvname\Scripts\activate".
```
IMP: Python version to be used is 3.9
```
4. Once activated, install all the packages using the command "pip install -r requirements.txt".
5. Once all packages are installed create a .env file with the following vars
```
VSCODE_LOCATION= (Location of Code.exe in your PC)
WEATHER_API_KEY= (Get it from https://openweathermap.org/api)
NEWS_API_KEY= (Get it from https://newsapi.org/)
EMAIL= (Email ID you want to send email from)
SECRET_KEY= (App Password of the email. Steps to get this given below)
RECEIVER_WHATSAPP_NUMBER= (Number whom you want to send the whatsapp message. Format: +91 Number)
WHATSAPP_MESSAGE= (Whatsapp message you want to send)
TIME_IN_24_HRS= (Time in hrs at which you to send the message. Eg: "21")
TIME_IN_MINS= (Time in mins at which you to send the message. Eg: "30". So message will be sent at 09:30pm)
```
6. Now you are ready to run the application. Type 'py alexa.py' in the terminal and hit enter.
7. A GUI created using pyqt5 will open. Clicking on the run button starts alexa.
8. Just say 'Alexa wake up' and your desktop assistant is ready to perform the tasks you ask to do it.


## Functions that ALEXA can perform/answer:  
1. Greeting Functions 
   - Who are you?  
   - How are you?  
   - Are you single?  
   - Do you love me?  
    
2. Basic questions  
   - What is the time?  
   - Today's date  
   - A Joke (Using pyjokes module) 
   - Weather in any place (Using openweathermap API)  
   - Current location (Using https://get.geojs.io/)
   - Internet speed (Using speedtest module)
   - IP address (Using https://api.ipify.org)
    
3. Tasks to be done on a browser  
   - Play songs on youtube (Using pywhatkit module's playonyt fn)
   - Open youtube (Using webbrowser module)    
   - Open google  
   - Open stack overflow  
    
4. Fetching Data  
   - Who is ____? Eg: Who is MS DHoni? (Using wikipedia module) 
   - Information on wikipedia. Eg: MS Dhoni Wikipedia  
   - Top 5 News headlines (Fetches from http://newsapi.org)  
   - Read any page of a particular pdf (PDF needs to be saved inside files folder and specified in pdf_reader function)
    
5. Control applications in windows (Using os module)   
   - Open visual studio code
   - Close visual studio code  
   - Open command prompt  
   - Open camera  
   - Open notepad  
   - Close notepad  
    
6. Automate social networks  
   - Send email to a particular person
      - Using SMTPlib module.
      - Expects to enter the mail ID of the person you want to send the email and the message  
   - Send whatsapp message
      - Using pywhatkit's module sendwhatmsg fn.
      - Expects to be logged into your whatsapp on whatsapp web
   - Check someone's Instagram profile and download profile picture
      - Using webbrower module & downloads picture using instaloader module.
      - Expects to enter the username
   - Tweet a tweet
      - Using script inside files/self_tweet.py which uses selenium for automation.
      - Expects your twitter credentials in files/twitter_info.txt and the message you want to tweet in the terminal.
      - **Unfortunately**, now with additional secruity measures imposed the script fails at 2 step authentication as it expects the OTP to be entered.
    
7. Basic window functions  
   - Switch the window (Using pyautogui module) 
   - Take a screenshot (Using pyautogui module)  
   - Hides all files in the current directory (Using os module) 
   - Unhide those hidden files (Using os module)
   - Check battery percentage (Using psutil module)  
    
8. Control volume of the system (Using pyautogui module)  
   - Volume up  
   - Volume down  
   - Mute and unmute  
    
9. Control power options of system (Using os module) 
   - Shut down the system  
   - Restart the system  
   - Put the system into sleep  
    
10. Other functions  
    - Simple Mathematical calculations (Expects the expression. Eg: 2 + 2) 
    - Wish someone on thier birthday with thier picture turned into a sketch  

## To create exe file of the project    
```
pyinstaller --onefile alexa.py
```  
Exe file with alexa as name could be found in dist folder

## Snapshots
![Screenshot (393)](https://github.com/pranith-rao/Alexa-Using-Python/assets/65860350/52571b06-c31b-4996-a3e4-7fa436b586d0)
![Screenshot (2028)](https://github.com/pranith-rao/Alexa-Using-Python/assets/65860350/14dda740-2609-4e4e-ba9e-8c1e8c0c9220)


