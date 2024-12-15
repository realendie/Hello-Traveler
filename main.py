from tkinter import *
import tkinter as tk
from gooey import Gooey, GooeyParser
import subprocess
import sys
import time

start = input('Old Man: yawn.... Oh hello there traveler! Would you like to play or die?\n')

# Corrected string comparison for "Play" or "play"
if start.lower() == 'play':
    print('Old Man: Wonderful lets play. What is your name?\n')
elif start.lower() == 'die':
    print('Lame, well, you die now.(Ending 1/6)')
    time.sleep(20)
    quit(code=1)
else:
    print('invalid response (Ending 0/6)')
    time.sleep(10)
    quit(code=0)

name = input()
setting = input(f'Old Man: Hello, {name} you like to go the attic or the basement?\n')

# Corrected string comparison for "Attic" or "attic"
if setting.lower() == 'attic':
    print('You walk up the stairs to the attic. You find a box...')
    box = input('Do you open the box or leave it to go explore?\n')
elif setting.lower() == 'basement':
    print('You fall down the stairs to the basement, hit your head and die. (Ending 2/6)')
    time.sleep(20)
    quit(code=2)
else:
    print('invalid response (Ending 0/6)')
    time.sleep(10)
    quit(code=0)

# Box handling - normalized to lowercase for user input
if box.lower() == 'explore' or box.lower() == 'leave it':
    print('The lights suddenly flicker, you feel around for anything and you find a flashlight.')
    light = input('You see two light switches, do you flick the left or the right one?\n')
elif box.lower() == 'open it' or box.lower() == 'open':
    print('You open the box, the old man then pushes you in and you die of suffocation. (Ending 3/6)')
    time.sleep(20)
    quit(code=3)
else:
    print('invalid response (Ending 0/6)')
    time.sleep(10)
    quit(code=0)

# Light switch handling - normalized to lowercase
if light.lower() == 'right':
    print('It does nothing, you flip the other switch.')
elif light.lower() == 'left':
    print('The light turns on... you see a dark shadowy figure in the corner')
else:
    print('invalid response (Ending 0/6)')
    time.sleep(10)
    quit(code=0)

# Attic corner figure handling - normalized to lowercase
figure = input('Do you approach it?\n')

if figure.lower() == 'yes':
    print('You walk towards the figure and reach out to it and realize that it\'s just a dusty old coat hanging on a hook.\n You feel a strange sense of disappointment almost as if you were expecting something more.')
    print('You turn to leave, but as you do you hear a faint whisper coming from the corner. You take a step back, your heart pounding in your chest.')
    next = input('You feel a chill run down your spine (Type "Next" to Continue)')
    
    if next.lower() == 'next':
        print('"You have found me", the voice whispers, "I have been waiting for you".')
        print('You walk towards the figure. You reach out and your fingers brush against the fabric. The shadow seems to grow.')
        print('You get pulled into the fabric and the shadow engulfs you. You feel a sharp pain, then everything goes black. (Ending 4/6)')
        time.sleep(20)
        quit(code=4)
    else:
        print('invalid response (Ending 0/6)')
        time.sleep(10)
        quit(code=0)

elif figure.lower() == 'no':
    print('Old Man: We should probably head downstairs now.')
else:
    print('invalid response (Ending 0/6)')
    time.sleep(10)
    quit(code=0)

# Downstairs again handling - normalized to lowercase
tea = input('Would you like some tea?')

if tea.lower() == 'yes':
    print('You wait for 10 minutes... the old man has not come back yet.')
    wait = input('Do you wait longer or do you leave out the front door?\n')
    
    if wait.lower() == 'wait':
        print('You wait 5 more minutes and he arrives with your tea.')
        print('You drink the entire mug of tea hastily. Everything then fades to black, you\'ve been poisoned. (Ending 5/6)')
        quit(code=5)
    elif wait.lower() == 'leave':
        print('You leave the house and hitchhike back to town.(Ending 6/6)')
    else:
        print('invalid response (Ending 0/6)')
        time.sleep(10)
        quit(code=0)

# Final outcome
print('You Survived!')
print('Thank you for playing. I hope you enjoyed!\n-endie')
quit(code=6)
