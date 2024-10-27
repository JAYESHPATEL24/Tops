import pyttsx3
import time

gf = pyttsx3.init()
 
rate = gf.getProperty('rate')
gf.setProperty('rate', rate - 50)  

gf.say("Hey Disha, WELCOME BACK!!!!!")
gf.runAndWait()

time.sleep(0.5)

gf.say("Hey Dishu, You are so cute.")
gf.runAndWait()

