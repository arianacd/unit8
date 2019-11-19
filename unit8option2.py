# by ariana daney
# last modified november 19, 2019
# this program creates a calculator

from tkinter import *
root = Tk()

title = Label(root, text="Calculator", font="Helvetica 24")
title.grid(row=1, column=1, columnspan=4)

result_bar = Entry()
result_bar.grid(row=2, column=1, columnspan=4)

clear_button = Button(root, text="Clear", width=5, font="Helvetica 14")
clear_button.grid(row=3, column=1)

negative_button = Button(root, text="+/-", width=5, font="Helvetica 14")
negative_button.grid(row=3, column=2)

percent_button = Button(root, text="%", width=5, font="Helvetica 14")
percent_button.grid(row=3, column=3)

divide_button = Button(root, text="/", width=5, font="Helvetica 14")
divide_button.grid(row=3, column=4)

seven = Button(root, text="7", width=5, font="Helvetica 14")
seven.grid(row=4, column=1)

eight = Button(root, text="8", width=5, font="Helvetica 14")
eight.grid(row=4, column=2)

nine = Button(root, text="9", width=5, font="Helvetica 14")
nine.grid(row=4, column=3)

times_button = Button(root, text="*", width=5, font="Helvetica 14")
times_button.grid(row=4, column=4)



root.mainloop()
