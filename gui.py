from tkinter import *
import tkinter as tk
import customtkinter
import subprocess
import sys

# widgets = Buttons, Text Boxes, Labels, Images, etc...
# windows = container for widgets

def submit():
   response = entry.get()
   print(response)
def submit(submit):
   response = entry.get()
   print(response)

window = Tk()
window.geometry('420x210')
window.title('Hello Traveller')
window.config(background='#111111')
window.bind('<Return>', submit)

#logo = PhotoImage(file='')
#window.iconphoto(True,logo)

terminal_prompt = Text(window, height=8)
terminal_prompt.config(bg='black', fg='white')
terminal_prompt.config(state=tk.DISABLED)
terminal_prompt.pack()

entry = Entry()
entry.config(font=('Monoscape', 15))
entry.config(bg='Black')
entry.config(fg='White')
entry.config(width=15)
entry.pack()

submit_button = Button(window,text='Submit')
submit_button.config(command=submit)
submit_button.config(font=('Monoscape', 10, 'bold'))
submit_button.config(bg='#111111')
submit_button.config(fg='white')
submit_button.config(activebackground='#00ff00')
submit_button.pack()

quit_button = Button(window,text='Quit')
quit_button.config(command=quit)
quit_button.config(font=('Monoscape', 10, 'bold'))
quit_button.config(bg='#111111')
quit_button.config(fg='white')
quit_button.config(activebackground='#ff0000')
quit_button.pack()

window.mainloop()