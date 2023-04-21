from tkinter import *


root = Tk()

"""
[      ]
1 2 3 C
4 5 6 /
7 8 9 *
+ 0 - =
"""

entry = Entry(root, width=20 ,relief=SUNKEN)
entry.grid(row=0, column=0, columnspan=4)

btn_collection = (
    ("1", "2", "3", "C"),
    ("4", "5", "6", "/"),
    ("7", "8", "9", "*"),
    ("+", "0", "-", "="),
)

def on_click(text):
    global entry
    entry.insert(0, text)

def partial(func, text):
    def wrapper():
        return func(text)

    return wrapper


for y, btns in enumerate(btn_collection):
    for x, btn in enumerate(btns):
        btn = Button(root, width=5, text=btn, command=partial(on_click, btn))
        btn.grid(row=y+1, column=x)









root.mainloop()