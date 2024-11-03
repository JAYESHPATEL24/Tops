from tkinter import *


class Title:
    def title(self,root):
        title = Label(self.root, text="Billing Software", font=("times new roman", 25, "bold"), bg="#074463", fg='white', bd=12, relief=GROOVE, pady=2)
        title.pack(fill=X)


class Bill_UI(Title):
    def __init__(self,root):
        self.root = root
        self.root.title("BILLING SOFTWARE")
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenwidth()}+{-7}+{0}")

        self.title(root)


class Customerdetalis:
    def __init__(self,root):
        pass


root = Tk()


go = Bill_UI(root)

root.mainloop()