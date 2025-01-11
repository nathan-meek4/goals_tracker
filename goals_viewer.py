import os
from tkinter import Tk, Label, Button, Text, filedialog, messagebox

GOALS_FILE = "goals.txt"

def load_goals():
    """Load goals from a file."""
    if os.path.exists(GOALS_FILE):
        with open(GOALS_FILE, "r") as file:
            return file.read()
    return "Enter your goals here..."

def save_goals():
    """Save the updated goals to a file."""
    with open(GOALS_FILE, "w") as file:
        file.write(goals_text.get("1.0", "end-1c"))  
    messagebox.showinfo("Success", "Goals saved successfully!")

def close_app():
    """Close the application."""
    root.destroy()

root = Tk()
root.title("Goals Manager")
root.geometry("400x400")

title_label = Label(root, text="Manage Your Goals", font=("Arial", 16), pady=10)
title_label.pack()

goals_text = Text(root, font=("Arial", 12), wrap="word", height=15, width=40)
goals_text.insert("1.0", load_goals())  
goals_text.pack(pady=10)

save_button = Button(root, text="Save Goals", command=save_goals, font=("Arial", 12))
save_button.pack(side="left", padx=10, pady=5)

close_button = Button(root, text="Close", command=close_app, font=("Arial", 12))
close_button.pack(side="right", padx=10, pady=5)

root.mainloop()
