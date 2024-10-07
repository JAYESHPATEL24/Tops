# Write a Python program to write a list to a file.

    # create a list with elements.    
l = ["If i can't See the Light ", "that Leads to The Goal. ", "Then i need to become the Light.", " Watch me", " I'll Devour it"," And Turn it into Light."]

    # open a file in write mode
with open("Goal.txt","w") as file:
        # write each element of list into a file.
    for i in l:
        file.write(i)