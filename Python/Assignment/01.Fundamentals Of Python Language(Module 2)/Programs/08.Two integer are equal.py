# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5. 

n1 = int(input("Enter the first Number  : "))

n2 = int(input("Enter the second Number : "))

# Check if the two integers are equal or their sum or difference is 5
if n1 == n2 or n1 + n2 == 5 or abs(n1 - n2) == 5:
    print(True)
else:
    print(False)
