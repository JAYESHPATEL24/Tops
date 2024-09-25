# Write a Python program to find the length of a tuple.  

t = (1, "Hello", 9.5, 6, 100, False, "Ok", "hi", 7.8)

l = 0
    # Find the length of tuple
for i in t:
    l += 1
    
    # Print the length of tuple
print(f"Length of Tuple =  {l} ")
