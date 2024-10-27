import pyttsx3

Student = pyttsx3.init()

# Set voice
voices = Student.getProperty('voices')
Student.setProperty('voice', voices[1].id)  

# Adjust the speech rate
rate = Student.getProperty('rate')
Student.setProperty('rate', rate - 50)  

Student.say("Good morning, Prashant sir. Jay Shree Ram.")
Student.runAndWait()


Student.say("You are looking handsome.")
Student.runAndWait()

