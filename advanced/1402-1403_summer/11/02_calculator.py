from tkinter import *
from tkinter import ttk # new widget style

# create root widget
root = Tk()
# root.geometry("400x400")

"""
[               ]
| 1 | 2 | 3 | / |
| 4 | 5 | 6 | * |
| 7 | 8 | 9 | + |
| C | 0 | = | - |
"""

buttons = [
    "1 2 3 /", 
    "4 5 6 *", 
    "7 8 9 +", 
    "C 0 = -"  
]

Font_tuple = ("Comic Sans MS", 10, "bold")

# widgets
# entry, button ?
entry = Entry(root, width=24, font=Font_tuple)
entry.grid(row=0, column=0, columnspan=4)

def partial_function(btn):
    # bind: btn to command
    def command():
        global entry
        
        if btn == "C":
            entry.delete(0, END)
        elif btn == "=":
            res = eval(entry.get())
            entry.delete(0, END)
            entry.insert(0, res)
        else:
            current = entry.get()
            entry.insert(len(current), btn)

    return command

for y, btns in enumerate(buttons):
    for x, btn in enumerate(btns.split()):
        button = Button(
            root,
            text=btn, 
            command=partial_function(btn), # func()
            width=10, 
            height=5, 
            font=Font_tuple
        )
        button.grid(row=y+1, column=x)


root.mainloop()

