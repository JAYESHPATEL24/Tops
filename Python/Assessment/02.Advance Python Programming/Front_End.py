from tkinter import *

    
class Bill_App_Base:

    def __init__(self,root):
        self.root = root

        x = root.winfo_screenwidth()
        y = root.winfo_screenheight()
        
        self.root.geometry(f"{x}x{y}")
        self.root.title("Billing Software")
        self.root.config(bg="white")
        self.titlecreation()

    def titlecreation(self):
        title = Label(self.root,text="Billing Software",font=("times new roman",25,"bold"),bg="#074463",fg = 'white',bd=12,relief=GROOVE,pady=2).pack(fill=X)


class Frames(Bill_App_Base):
    def __init__(self, root):
        super().__init__(root)

class Labels(Frames):
    def __init__(self,root):
        super().__init__(root)

class InputBoxs(Frames):
    def __init__(self, root):
        super().__init__(root)

class Buttons(Frames):
    def __init__(self, root):
        super().__init__(root)

class Billingsoftware(Labels,InputBoxs,Buttons):
    def __init__(self, root):
        super().__init__(root)

root = Tk()
bill = Billingsoftware(root) 
root.mainloop()