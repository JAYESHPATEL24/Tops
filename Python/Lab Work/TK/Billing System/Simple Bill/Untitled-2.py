print("\n","="*20)
import os

if not os.path.exists("Sysbills"): 
    os.makedirs("Sysbills") # Check if each .txt file exists in the folder and create if it doesn't 
file_path = os.path.join("Sysbills", "1004.txt") 
if not os.path.exists(file_path):
    with open(file_path, 'w') as file:
        file.write('This is a sample text file.')
else:
    print("pahela thi 6e")

file = open("Bills\\Good.txt","w")
file.write("Hello Beautiful World!!!!!!")
file.close()