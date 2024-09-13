import time
import datetime

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Wake up!")
            break
        time.sleep(1)

alarm_time = input("Enter the time to set the alarm (HH:MM:SS): ")
set_alarm(alarm_time)
