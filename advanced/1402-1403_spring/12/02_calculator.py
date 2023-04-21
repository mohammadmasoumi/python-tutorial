from tkinter import *
from functools import partial

root = Tk()

"""
[      ]
1 2 3 C
4 5 6 /
7 8 9 *
+ 0 - =
"""

entry = Entry(root, width=20, relief=SUNKEN)
entry.grid(row=0, column=0, columnspan=4)

btn_collection = (
    ("1", "2", "3", "C"),
    ("4", "5", "6", "/"),
    ("7", "8", "9", "*"),
    ("+", "0", "-", "="),
)

operators = ("+", "-", "/","*")
fnumber, opt, snumber = None, None, None

def calc():

    if opt == "+":
        return fnumber + snumber
    elif opt == "-":
        return fnumber - snumber
    if opt == "*":
        return fnumber * snumber
    elif opt == "/":
        return fnumber / snumber

def on_command(btn_text):
    global entry, fnumber, opt, snumber

    entry.insert(len(entry.get()), btn_text)
    curr = entry.get()
    
    if btn_text in operators:
        fnumber = int(curr[:-1]) 
        opt = btn_text
    elif btn_text == "=":
        snumber = int(curr[curr.index(opt)+1: -1])
        entry.delete(0, END)
        entry.insert(0, calc())

    elif btn_text == "C":
        fnumber, opt, snumber = None, None, None
        entry.delete(0, END)

# def partial(f, **options):
#     def wrapper():
#         return f(**options)
#     return wrapper

for y, collection in enumerate(btn_collection):
    for x, btn_text in enumerate(collection):
        btn = Button(root, text=btn_text, width=5, command=partial(on_command, btn_text), relief=RAISED)
        btn.grid(row=y+1, column=x)

root.mainloop()