# import pygame,sys
from tkinter import *
# pygame.init()
from PIL import Image, ImageTk
expression = ""

def clear():
	global expression
	expression = ""
	equation.set("")

def press(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("error")
        expression = ""

if __name__ == "__main__":

    button_width = 10
    button_height = 1
    gui_width = 400
    gui_height = 647
# create GUI
    gui = Tk()
    gui.title("Nguyen's calculator") # name
    gui.configure(width= gui_width, height= gui_height) # height and width: 1/1.628 là tỷ lệ vằng
    # load
    # img = Label(gui, image=)

# create Entry
    equation = StringVar()
    label = Entry(gui, textvariable=equation, width=40)
    label.grid(columnspan=60)
    # button_frame = Frame(gui).pack(side= BOTTOM)
# create frame1
    button1 = Button(gui, text=' 1 ', fg='black', bg='red', command=lambda: press(1),  height=button_height, width=button_width)
    button1.grid(row=2, column=0)
    
    button2 = Button(gui, text=' 2 ', fg='black', bg='red', command=lambda: press(2), height=button_height, width=button_width)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg='black', bg='red', command=lambda: press(3), height=button_height, width=button_width)
    button3.grid(row=2, column=2)

    plus = Button(gui, text=' + ', fg='black', bg='red', command=lambda: press('+'), height=button_height, width=button_width)
    plus.grid(row=2, column=3)

# create frame2
    button4 = Button(gui, text=' 4 ', fg='black', bg='red', command=lambda: press(5), height=button_height, width=button_width)
    button4.grid(row=4, column=0)

    button5 = Button(gui, text=' 5 ', fg='black', bg='red', command=lambda: press(5), height=button_height, width=button_width)
    button5.grid(row=4, column=1)

    button6 = Button(gui, text=' 6 ', fg='black', bg='red', command=lambda: press(6), height=button_height, width=button_width)
    button6.grid(row=4, column=2)

    minus = Button(gui, text=' - ', fg='black', bg='red', command=lambda: press("-"), height=button_height, width=button_width)
    minus.grid(row=4, column=3)

# create frame3
    button7 = Button(gui, text=' 7 ', fg='black', bg='red', command=lambda: press(button_width), height=button_height, width=button_width)
    button7.grid(row=6, column=0)

    button8 = Button(gui, text=' 8 ', fg='black', bg='red', command=lambda: press(8), height=button_height, width=button_width)
    button8.grid(row=6, column=1)

    button9 = Button(gui, text=' 9 ', fg='black', bg='red', command=lambda: press(9), height=button_height, width=button_width)
    button9.grid(row=6, column=2)

    multiply = Button(gui, text=' * ', fg='black', bg='red', command=lambda: press("*"), height=button_height, width=button_width)
    multiply.grid(row=6, column=3)

# create frame4
    Delete = Button(gui, text=' C ', fg='black', bg='red', command=clear, height=button_height, width=button_width)
    Delete.grid(row=8, column=0)

    button0 = Button(gui, text=' 0 ', fg='black', bg='red', command=lambda: press(0), height=button_height, width=button_width)
    button0.grid(row=8, column=1)

    decimal = Button(gui, text=' . ', fg='black', bg='red', command=lambda: press("."), height=button_height, width=button_width)
    decimal.grid(row=8, column=2)

    divide = Button(gui, text=' / ', fg='black', bg='red', command=lambda: press("/"), height=button_height, width=button_width)
    divide.grid(row=8, column=3)

# create frame5
    equal = Button(gui, text=' = ', fg='black', bg='red', command=equalpress, height=button_height, width=button_width*4)
    equal.grid(row=10, column=0, columnspan=4)

    gui.mainloop()
