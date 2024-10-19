import tkinter as tk
import random

# List of gift ideas
gifts = [
    "Personalized Notebook",
    "Gift Card to a Favorite Bookstore",
    "Self-Development Book",
    "Customized Mug",
    "Workshop or Online Course",
    "Personalized Pen",
    "Thank You Plant",
    "Handwritten Letter"
]

def suggest_gift():
    """Suggest a random gift from the list."""
    suggested_gift = random.choice(gifts)
    gift_label.config(text=suggested_gift)

# Set up the main application window
root = tk.Tk()
root.title("Gift Suggestion for Teacher")

# Create and place a label for the suggestion
gift_label = tk.Label(root, text="Click the button for a gift suggestion!", wraplength=300)
gift_label.pack(pady=20)

# Create and place a button to suggest a gift
suggest_button = tk.Button(root, text="Suggest Gift", command=suggest_gift)
suggest_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
