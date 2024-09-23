# Write a Python program to count occurrences of a substring in a string.

        # user inputs
s = input("Enter the main string: ")
sub = input("Enter the substring: ")

count = 0
start = 0
sl = 0   

        #count the length of main string. 
for i in s:  
    sl+=1

        # Loop through the main string to find sub string occurrences
while start < sl:
    pos = s.find(sub, start)
    if pos != -1:
        count += 1
        start = pos + 1
    else:
        break


print(f"Number of overlapping occurrences of '{sub}' in '{s}': {count}")

