import pyttsx3

gf = pyttsx3.init()

rate = gf.getProperty('rate')
gf.setProperty('rate', rate - 50)  

gf.say("Hey mahi, Su kaare chhae?")

gf.runAndWait()