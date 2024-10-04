# Find the middle of string through the parameterized function.

def middle(s):
    
    middle = len(s)//2
    
    return s[middle]

str = input("Enter a String : ")

print(f"Middle Character of String : {middle(str)}")