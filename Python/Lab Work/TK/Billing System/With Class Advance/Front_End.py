from tkinter import *

    # Base Window class to set up the main application window class Window
class Window:
    def __init__(self,root):
        self.root = root
             # Set the window title
        self.root.title("BILLING SOFTWARE")
            # Set window to full screen
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenwidth()}+{-7}+{0}")


    # Class for the title section of the window
class Title(Window):
    def __init__(self, root):
        super().__init__(root)
        self.title()

        # Method to create the title label def title
    def title(self):
        title = Label(self.root, text="Billing Software", font=("times new roman", 25, "bold"), bg="#074463", fg='white', bd=12, relief=GROOVE, pady=2)
        title.pack(fill=X)


    # CustomerDetails class to set up customer details UI elements class
class CustomerDetails(Title):
    def __init__(self, root):
        super().__init__(root)
        self.create_frame()
        self.Customerdetails_Labels()

    def create_frame(self):
        self.Customer_details = LabelFrame(root, text=" Customer Details ", font=("arial", 12, "bold"), bg="#074463", fg="gold", relief=GROOVE, bd=5)
        self.Customer_details.place(x=0, y=70, relwidth=1)

    def Customerdetails_Entries(self):


    # Class for the billing UI
class Bill_UI(CustomerDetails):
    def __init__(self, root):
        super().__init__(root)



root = Tk()


go = Bill_UI(root)

root.mainloop()