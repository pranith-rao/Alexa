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
