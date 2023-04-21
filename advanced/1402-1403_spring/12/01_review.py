from tkinter import *

root = Tk()

label = Label(root, text="Hello")
# label.pack()
label.grid(row=0, column=0)

button = Button(root, text="clickme!", command=lambda : print("Clicked"))
button.grid(row=0, column=1)

root.mainloop()