
# by ariana daney
# last modified november 20, 2019
# this program creates a calculator

from tkinter import *
root = Tk()


def add_zero():
    new_result = display_result.get()
    new_result += "0"
    display_result.set(new_result)


def add_one():
    new_result = display_result.get()
    new_result += "1"
    display_result.set(new_result)


def add_two():
    new_result = display_result.get()
    new_result += "2"
    display_result.set(new_result)


def add_three():
    new_result = display_result.get()
    new_result += "3"
    display_result.set(new_result)


def add_four():
    new_result = display_result.get()
    new_result += "4"
    display_result.set(new_result)


def add_five():
    new_result = display_result.get()
    new_result += "5"
    display_result.set(new_result)


def add_six():
    new_result = display_result.get()
    new_result += "6"
    display_result.set(new_result)


def add_seven():
    new_result = display_result.get()
    new_result += "7"
    display_result.set(new_result)


def add_eight():
    new_result = display_result.get()
    new_result += "8"
    display_result.set(new_result)


def add_nine():
    new_result = display_result.get()
    new_result += "9"
    display_result.set(new_result)


def clear():
    clear_num = ""
    display_result.set(clear_num)


def divide():
    new_result = display_result.get()
    new_result += "/"
    display_result.set(new_result)


def percent():
    new_result = display_result.get()
    new_result = float(new_result) / 100
    display_result.set(new_result)


def negative():
    new_result = display_result.get()
    new_result = float(new_result) * -1
    display_result.set(new_result)


def times():
    new_result = display_result.get()
    new_result += "*"
    display_result.set(new_result)


def subtract():
    new_result = display_result.get()
    new_result += "-"
    display_result.set(new_result)


def add():
    new_result = display_result.get()
    new_result += "+"
    display_result.set(new_result)


def decimal_point():
    new_result = display_result.get()
    new_result += "."
    display_result.set(new_result)


def equal():
    new_result = display_result.get()
    new_result = eval(new_result)
    display_result.set(new_result)


title = Label(root, text="Calculator", font="Helvetica 24")
title.grid(row=1, column=1, columnspan=4)

display_result = StringVar()
result_bar = Entry(root, textvariable=display_result, justify="right")
result_bar.grid(row=2, column=1, columnspan=4)

clear_button = Button(root, text="Clear", width=5, font="Helvetica 14", command=clear)
clear_button.grid(row=3, column=1)

negative_button = Button(root, text="+/-", width=5, font="Helvetica 14", command=negative)
negative_button.grid(row=3, column=2)

percent_button = Button(root, text="%", width=5, font="Helvetica 14", command=percent)
percent_button.grid(row=3, column=3)

divide_button = Button(root, text="/", width=5, font="Helvetica 14", command=divide)
divide_button.grid(row=3, column=4)

seven = Button(root, text="7", width=5, font="Helvetica 14", command=add_seven)
seven.grid(row=4, column=1)

eight = Button(root, text="8", width=5, font="Helvetica 14", command=add_eight)
eight.grid(row=4, column=2)

nine = Button(root, text="9", width=5, font="Helvetica 14", command=add_nine)
nine.grid(row=4, column=3)

times_button = Button(root, text="*", width=5, font="Helvetica 14", command=times)
times_button.grid(row=4, column=4)

four = Button(root, text="4", width=5, font="Helvetica 14", command=add_four)
four.grid(row=5, column=1)

five = Button(root, text="5", width=5, font="Helvetica 14", command=add_five)
five.grid(row=5, column=2)

six = Button(root, text="6", width=5, font="Helvetica 14", command=add_six)
six.grid(row=5, column=3)

minus = Button(root, text="-", width=5, font="Helvetica 14", command=subtract)
minus.grid(row=5, column=4)

one = Button(root, text="1", width=5, font="Helvetica 14", command=add_one)
one.grid(row=6, column=1)

two = Button(root, text="2", width=5, font="Helvetica 14", command=add_two)
two.grid(row=6, column=2)

three = Button(root, text="3", width=5, font="Helvetica 14", command=add_three)
three.grid(row=6, column=3)

plus = Button(root, text="+", width=5, font="Helvetica 14", command=add)
plus.grid(row=6, column=4)

zero = Button(root, text="0", width=5, font="Helvetica 14", command=add_zero)
zero.grid(row=7, column=1)

decimal = Button(root, text=".", width=5, font="Helvetica 14", command=decimal_point)
decimal.grid(row=7, column=2)

equals = Button(root, text="=", width=11, font="Helvetica 14", command=equal)
equals.grid(row=7, column=3, columnspan=2)


root.mainloop()