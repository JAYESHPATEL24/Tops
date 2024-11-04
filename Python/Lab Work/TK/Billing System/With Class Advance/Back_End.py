from tkinter import En

class PlaceholderEntry(Entry):
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
