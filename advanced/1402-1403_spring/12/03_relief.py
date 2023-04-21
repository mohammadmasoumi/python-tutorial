from tkinter import *

root = Tk()

# FLAT
# RAISED
# SUNKEN
# GROOVE
# RIDGE

frame = Frame(root, width=50, height=50)
frame.grid(row=0, column=0)

label1 = Label(frame, text="label1", bg="red", padx=50, pady=50, relief=GROOVE)
label1.grid(row=0, column=0)

label2 = Label(frame, text="label2", bg="yellow", padx=50, pady=50, relief=RIDGE)
label2.grid(row=0, column=1)

root.mainloop()