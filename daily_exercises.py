# by ariana daney
# last modified november 15, 2019
# unit 8 daily exercises

from tkinter import *

root = Tk()

# ex. 1
# hello_world = Label(root, text="Hello, World")
# hello_world.grid(row=1, column=1)

# ex. 2
user_name = StringVar
greeting = Entry(root)
greeting.grid(row=1, column=1)
hello_greeting = Label(root, text="Hello," + user_name)
root.mainloop()
