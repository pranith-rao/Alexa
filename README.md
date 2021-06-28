# Alexa-Using-Python

This is a desktop assistant built using Python and sapi5 for text to speech convertor.   
Lot of modules are used in this program for different purposes.  
When you run the program a window will pop up i.e. the alexa interface with run and exit buttons.   
When you press the run button program execution starts and alexa will initially be in sleep mode.   
You have to say ALEXA WAKE UP to activate alexa.  
You have to wait for Alexa is listening... to be printed in terminal before saying an command. Else command wont be executed properly.  
Any command said to converted into text using the google api and converted into lowercase.  
That lowercase command will be compared to the ones mentioned in the if-else ladder and carry out the task described in its indentation.  
If a particular command is not found alexa will simple say "Sorry i dont know that" and wait for the next command.  
You can say sleep to put alexa back into sleep and stop to shutdown alexa.  

## To create exe file of the project  
Clone this project to a folder  
Open cmd prompt with the folder containing this project as current directory  
And type:  
   pip install pyinstaller  
   pyinstaller --onefile alexa,py  
Done, exe file with alexa.py as name could be found in dist folder   



## Functions that our ALEXA can perform:  
1). Greeting Functions:  
    * Who are you?  
    * How are you?  
    * Are you single?  
    * Do you love me?  
    
2). Basic questions  
    * What is the time?  
    * Today's date  
    * A Joke  
    * Weather in any place  
    * Current location  
    * Internet speed  
    * IP address  
    
3). Tasks to be done on chrome  
    * Play sons on youtube  
    * Open youtube    
    * Open google  
    * Open stack overflow  
    
4). Fetching Data  
    * Who is ____? Eg: Who is MS DHoni?  
    * Information on wikipedia. Eg: MS Dhoni Wikipedia  
    * Top 5 News headlines  
    * Read any page of a particular pdf  
    
5). Control applications in windows  
    * Open visual studio code
    * Close visual studio code  
    * Open command prompt  
    * Open camera  
    * Open notepad  
    * Close notepad  
    
 6). Automate social networks  
    * Send email to a particular person  
    * Send whatsapp message  
    * Check someone's Instagram profile and download profile picture  
    * Tweet a tweet  
    
7). Basic window functions  
    * Switch the window  
    * Take a screenshot  
    * Hides all files in the current directory  
    * Unhide those hidden files  
    * Check battery percentage  
    
8). Control volume of the system  
    * Volume up  
    * Volume down  
    * Mute and unmute  
    
9). Control power options of system  
    * Shut down the system  
    * Restart the system  
    * Put the system into sleep  
    
10). Other functions  
    * Simple Mathematical calculations  
    * Wish someone on thier birthday with thier picture turned into a sketch  
    
Lastly,  
11). Functions to control alexa  
    * Sleep will put alexa back into sleep mode  
    * Stop or thank you will shut down alexa completely  
    
    

