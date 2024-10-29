import tkinter as tk

def on_entry_click(event):
    if ename.get() == 'Enter your name':
        ename.delete(0, tk.END)  # delete all the text in the entry
        ename.config(fg='black')  # change text color to black

def on_focusout(event):
    if ename.get() == '':
        ename.insert(0, 'Enter your name')  # insert placeholder
        ename.config(fg='gray')  # change text color to gray

root = tk.Tk()
root.geometry("700x400")

name = tk.Label(root, text="Name", font=("Calibri", 20, "bold"), bg="lightblue")
name.place(x=50, y=50)

ename = tk.Entry(root, bg="lightgray", font=("Calibri", 20, "bold"))
ename.place(x=300, y=50, height=40, width=300)

# Set placeholder text
ename.insert(0, 'Enter your name')
ename.config(fg='gray')

# Bind events to show and hide placeholder
ename.bind('<FocusIn>', on_entry_click)
ename.bind('<FocusOut>', on_focusout)

root.mainloop()

# *************************2nd
import tkinter as tk

def on_entry_click(event, entry):
    if entry.get() == 'Enter your name':
        entry.delete(0, "end")  # delete all the text in the entry
        entry.config(fg='black')

def on_focusout(event, entry):
    if entry.get() == '':
        entry.insert(0, 'Enter your name')
        entry.config(fg='grey')

root = tk.Tk()
root.geometry("700x150")
root.title("Entry Placeholder Example")

name = tk.Label(root, text="Name", font=("Calibri", 20, "bold"), bg="lightblue")
name.place(x=50, y=50)
ename = tk.Entry(root, bg="lightgray", font=("Calibri", 20, "bold"))
ename.place(x=300, y=50, height=40, width=300)

ename.insert(0, 'Enter your name')
ename.config(fg='grey')
ename.bind('<FocusIn>', lambda event: on_entry_click(event, ename))
ename.bind('<FocusOut>', lambda event: on_focusout(event, ename))

root.mainloop()
