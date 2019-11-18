# by ariana daney
# last modified november 15, 2019
# unit 8 daily exercises

from tkinter import *

root = Tk()

# ex. 1
# hello_world = Label(root, text="Hello, World")
# hello_world.grid(row=1, column=1)

# ex. 2


def say_hi():
    if user_name == "":
        print("you forgot to enter to your name")
    else:
        print("hello", user_name)


user_name = StringVar()
entry_name = Entry(root, textvariable=user_name)
entry_name.grid(row=1, column=1)
hello = Label(root)
hello.grid(row=2, column=1)
say_hello = Button(root, text="Say Hello")
say_hello.grid(row=3, column=1)

root.mainloop()
