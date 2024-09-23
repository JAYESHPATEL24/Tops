# Write a Python program to count the number of strings where the string length is 2 or more and the first 
# and last character are same from a given list of strings.  

n = int(input("How many strings you wants to enter ? : "))

l = [] 

for i in range(n):
    s = input("Enter a String : ")
    l.append(s) 
    
count = 0 

for i in l:
    if len(i) > 2 and i[0] == i[-1]:
          count += 1

print(f"The number of string with matching first and last character : {count} ")          