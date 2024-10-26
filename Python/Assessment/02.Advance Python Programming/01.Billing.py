from tkinter import *

root = Tk()

root.geometry("10000x10000")
root.title("Billing Software")
root.config(bg="white")

frame = Frame(root, bg="darkblue", width=200, height=100, bd=7, )
frame.place(x=0, y=0, relwidth=1)
# frame.pack(padx=10, pady=10)

label = Label(frame, text="Billing Software", bg="darkblue", fg="white")
label.pack()

# label =  Label(root, text="Billing Software", font=("Arial",20,"bold"), anchor="center", fg="white")
# label.place(relheight=1, relwidth=1)

root.mainloop()