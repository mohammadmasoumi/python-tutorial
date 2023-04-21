from tkinter import *

root = Tk()


# create a frome
frame1 = Frame(root, padx=10, pady=10, border=2,  bd=2, bg="red", width=10)
frame1.grid(row=0, column=0)

frame2 = Frame(root, padx=50, pady=10, border=2,  bd=2, bg="yellow", width=50, relief=SUNKEN)
frame2.grid(row=0, column=1)

frame20 = Frame(frame2, padx=10, pady=10, border=2,  bd=2, bg="brown", width=25)
frame20.grid(row=0, column=0)

frame21 = Frame(frame2, padx=10, pady=10, border=2,  bd=2, bg="purple", width=25)
frame21.grid(row=1, column=0)


frame3 = Frame(root, padx=10, pady=10, border=2,  bd=2, bg="blue", width=50)
frame3.grid(row=1, column=0)

frame4 = Frame(root, padx=10, pady=10, border=2,  bd=2, bg="orange", width=50)
frame4.grid(row=1, column=1)

frame5 = Frame(root, padx=10, pady=10, border=2,  bd=2, bg="green", width=50)
frame5.grid(row=1, column=2)

# label
label = Label(frame1, text="Hello world!")
label.grid(row=1, column=0)

# label
label = Label(frame20, text="Hello world!")
label.grid(row=1, column=0)

# label
label = Label(frame21, text="Hello world!")
label.grid(row=1, column=0)

# label
label = Label(frame3, text="Hello world!")
label.grid(row=1, column=0)

# label
label = Label(frame4, text="Hello world!")
label.grid(row=1, column=0)

# label
label = Label(frame5, text="Hello world!")
label.grid(row=1, column=0)


root.mainloop()
