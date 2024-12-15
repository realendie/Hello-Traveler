from tkinter import *
import tkinter as tk
import customtkinter as ctk
import subprocess
import sys

# Configure appearance mode (optional: 'System', 'Dark', 'Light')
ctk.set_appearance_mode("Dark")  # Dark mode
ctk.set_default_color_theme("blue")  # Default theme

# Function to handle the submit button click
def submit():
    response = entry.get()
    print(response)

def submit_event(event):
    submit()

# Create the main application window
window = ctk.CTk()
window.geometry('420x250')
window.title('Hello Traveler')

window.iconbitmap("Hello_Traveler_Logo.ico")

# Create a read-only text box (terminal prompt)
terminal_prompt = ctk.CTkTextbox(window, height=100, state="disabled")
terminal_prompt.pack(pady=10)

# Create an entry box
entry = ctk.CTkEntry(window, placeholder_text="Enter your text", width=200, font=("Monospace", 15))
entry.pack(pady=5)

# Bind the Enter key to the submit function
window.bind('<Return>', submit_event)

# Create a Submit button
submit_button = ctk.CTkButton(window, text='Submit', command=submit, font=("Monospace", 12, "bold"))
submit_button.pack(pady=5)

# Create a Quit button
quit_button = ctk.CTkButton(window, text='Quit', command=window.quit, font=("Monospace", 12, "bold"), fg_color="red")
quit_button.pack(pady=5)

# Run the application
window.mainloop()
