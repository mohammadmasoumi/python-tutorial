import time
import threading
from tkinter import *
from random import shuffle
from functools import partial
from PIL import ImageTk, Image

root = Tk()

fruits = [
    "peach", "peach", "cherry", "cherry",
    "coconut","coconut", "pieapple", "pieapple", 
    "apple", "apple", "orange", "orange",
    "banana", "banana", "pomegranate", "pomegranate"
]

shuffle(fruits)

"""
1. create fruits shuffle
2. create buttons
3. create oncommand

"""
fbtn, sbtn = None, None

def compare():
    global fbtn, sbtn

    while True:
        if fbtn and sbtn:
            time.sleep(0.5)

            if fbtn.cget('text') == sbtn.cget('text') and fbtn.cget('text') != "":
                fbtn.configure(state=DISABLED)
                sbtn.configure(state=DISABLED)
            else:
                fbtn.configure(text="", state=NORMAL)
                sbtn.configure(text="", state=NORMAL)
            
            fbtn, sbtn = None, None


thread = threading.Thread(target=compare)
thread.start()

def on_command(btn, x, y):
    global fbtn, sbtn

    fruit = fruits[y*4+x]
    imagefile = f'C:\\Users\\MFT SERVER\\Desktop\\Python\\advanced-python-winter1401\\12\\images\\test.png'
    # img = ImageTk.PhotoImage(Image.open(u))  
    image= PhotoImage(file=imagefile, width=10, height=5)

    btn.configure(image=image, state=DISABLED)

    if not fbtn:
        fbtn = btn
    elif not sbtn:
        sbtn = btn 

for y in range(4):
    for x in range(4):
        btn = Button(root, text="", width=10, height=5, relief=SUNKEN)
        btn.grid(row=y, column=x)
        btn.configure(command=partial(on_command, btn, x, y))

root.mainloop()