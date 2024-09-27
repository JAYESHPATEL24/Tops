# Write a Python function that checks whether a passed string is palindrome or not 

    # python function for check string is palindrome or not.
def palindrome(s):
    if s == s[::-1]:
        print("String is Palindrome..")
    else:
        print("String is not palindrome..")
        
    
    # Get String from user.
s = input("Enter a String : ")

    # function call
palindrome(s)  
