# Write a Python program to check a list is empty or not.

        # function for check list is empty or not
def check_list(list):
    if not list:
        print("List is empty.")
    else:
        print("List is not empty.")
        
        
l = []
l1 = ["Hello", "beautiful", "World", 1, 2] 
l3 = []
l4 = [4.5,3.5,1,2,True]

        # function call
check_list(l)
check_list(l1)
check_list(l3)
check_list(l4)
    