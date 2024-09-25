# Write a Python program to convert a list to a tuple. 

l = []

    # Get user input for length of list.
n = int(input("Enter a length list : "))

    # Get list elements from user.
for i in range(n):
    a = input("Enter a Element : ")
    l.append(a)
    
    # Convert List into Tuple.
t = tuple(l) 

print(f"Entered List : {l}")
print("After Converting the List into Tuple.....")
print(f"Tuple : {t}")