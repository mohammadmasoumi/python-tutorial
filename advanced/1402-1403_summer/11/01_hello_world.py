from tkinter import *
from tkinter import ttk # new widget style

# create root widget
root = Tk()

# root.geometry("400x400")

# create a frome
frame1 = Frame(root, width=100, height=50, bg="red")
frame1.grid(row=0, column=0)
# frame1.place(x=-100, y=-100)

# frame2 = Frame(root, padx=10, pady=100, bg="yellow")
# frame2.grid(row=0, column=1)

# label
# label = Label(frame1, text="Hello world!")
# label.grid(row=1, column=0)

# button
"""
Cursor values:
"arrow"
"circle"
"clock"
"cross"
"dotbox"
"exchange"
"fleur"
"heart"
"heart"
"man"
"mouse"
"pirate"
"plus"
"shuttle"
"sizing"
"spider"
"spraycan"
"star"
"target"
"tcross"
"trek"
"watch"
"""

"""
relief values

SUNKEN , RAISED , GROOVE , RIDGE , and FLAT
"""

button = Button(
    frame1, 
    text="Exit", 
    command=root.destroy, 
    width=25, 
    height=12, 
    bg="green",
    cursor="heart"
)
button.grid(row=0, column=0)

# button
button = Button(frame1, text="Exit", command=lambda : print("Hello"), width=25, height=12)
button.grid(row=0, column=1)

# button
button = Button(frame1, text="Exit", command=root.destroy, width=25, height=12)
button.grid(row=1, column=0)

# button
button = Button(frame1, text="Exit", command=root.destroy, width=25, height=12)
button.grid(row=1, column=1)

frame2 = Frame(root, width=100, height=50, bg="red")
frame2.grid(row=0, column=1)

# button
button = Button(frame2, text="Exit", command=root.destroy, width=25, height=12, bg="green")
button.grid(row=0, column=0)

# button
button = Button(frame2, text="Exit", command=lambda : print("Hello"), width=25, height=12)
button.grid(row=0, column=1)

# button
button = Button(frame2, text="Exit", command=root.destroy, width=25, height=12)
button.grid(row=1, column=0)

# button
button = Button(frame2, text="Exit", command=root.destroy, width=25, height=12)
button.grid(row=1, column=1)

# label
# label = Label(frame2, text="Hello world!")
# label.grid(row=1, column=0)

# # label
# label = Label(frame2, text="Hello world!")
# label.grid(row=0, column=1)

# # button
# button = Button(frame2, text="Exit", command=root.destroy)
# button.grid(row=2, column=0)

# create loop
root.mainloop()