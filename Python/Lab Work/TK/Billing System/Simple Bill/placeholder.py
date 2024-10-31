import tkinter as tk

class PlaceholderEntry(tk.Entry):
    def __init__(self, master=None, placeholder="", *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.bind("<FocusIn>", self.on_focus)
        self.bind("<FocusOut>", self.on_focus_out)
        self.insert(0, self.placeholder)
        self.config(fg="grey")

    def on_focus(self, event):
        if self.get() == self.placeholder:
            self.delete(0, tk.END)
            self.config(fg="black")

    def on_focus_out(self, event):
        if not self.get():
            self.insert(0, self.placeholder)
            self.config(fg="grey")

root = tk.Tk()

# Create Entry fields with placeholders
name_entry = PlaceholderEntry(root, placeholder="Enter your name")
name_entry.pack(pady=10)

number_entry = PlaceholderEntry(root, placeholder="Enter your number")
number_entry.pack(pady=10)

bill_entry = PlaceholderEntry(root, placeholder="Enter your bill number")
bill_entry.pack(pady=10)

root.mainloop()
