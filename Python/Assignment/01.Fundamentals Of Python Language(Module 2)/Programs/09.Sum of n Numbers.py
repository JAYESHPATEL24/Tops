# Write a python program to sum of the first n positive integers.  

n = int(input("Enter any Number : "))

sum = 0
for i in range(n+1):    # calculate sum of n integer Numbers.
    sum += i
    
print(f"Sum of first {n} numbers = {sum}")