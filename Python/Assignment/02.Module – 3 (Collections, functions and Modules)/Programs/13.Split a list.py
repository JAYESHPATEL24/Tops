# Write a Python program to split a list into different variables.  

l = [] 

    # Get the length of the list from the user.
n = int(input("Enter a Length of List : "))

    # Get elements for the list From the user.
for i in range(n):
    e = input("Enter a element : ")
    l.append(e)
    
split_List = {}

    # split list and store it in separate variable using dictionary.
for i in range(n):
    split_List[chr(65+i)] = l[i]
    
    # print each variable with its value.
for key,value in split_List.items():
    print(f"{key} : {value}")
    
    
