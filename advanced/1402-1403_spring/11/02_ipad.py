from tkinter import *

root = Tk()

# create a frome
frame1 = Frame(root, padx=10, pady=10, border=2,  bd=2, bg="red", width=10)
frame1.grid(row=0, column=0)


label = Label(frame1, text="Hello world!")
label.grid(row=0, column=0)

btn = Button(frame1, text="Exit", command=root.destroy)
btn.grid(row=0, column=1)


root.mainloop()