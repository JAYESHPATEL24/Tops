from tkinter import *

def validate_name(input_str):
    print("Hello")
    if all(char.isalpha() or char.isspace() for char in input_str):
        return True
    return False

def click(event):
    if entry.get() == placeholder:
        entry.delete(0,END)
        entry.config(fg="black")

def unclick(event):
    if not entry.get():
        entry.insert(0,"Enter a Name")
        entry.config(fg="gray")


root = Tk()
placeholder = "Enter a Name"
label = Label(root, text = "Name",font=("Arial",20))
label.grid(row=0,column=0)

validate_cmd = root.register(validate_name)

entry = Entry(root,font=("Arial",20), validate="key", validatecommand=(validate_cmd,'%P'))
entry.grid(row=0,column=1)
entry.insert(0,placeholder)
entry.config(fg="gray")
entry.bind("<FocusIn>",click)
entry.bind("<FocusOut>",unclick)

label = Label(root, text = "Phone",font=("Arial",20))
label.grid(row=0,column=2)

pentry = Entry(root,font=("Arial",20))
pentry.grid(row=0,column=3)


root.mainloop()



