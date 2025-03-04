
import math
from tkinter import *

from cv2 import resize
root = Tk()
root.title("simple Calculator!!")
root.resizable(False,False)
e = Entry(root, width=40, borderwidth=5)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number)) 

def button_clean():
    e.delete(0,END)

def button_add():
    first_number = e.get()
    global first_num
    global math
    math = "addition"
    first_num = int(first_number)
    e.delete(0,END)

def button_equ():
    second_number = e.get()
    e.delete(0,END)
    if math=="addition":
        e.insert(0,first_num + int(second_number))

    if math=="subtraction":
        e.insert(0,first_num - int(second_number))

    if math=="multiplication":
        e.insert(0,first_num * int(second_number))

    if math=="division":
        e.insert(0,first_num / int(second_number))

    
def button_diff():
    first_number = e.get()
    global first_num
    global math
    math = "subtraction"
    first_num = int(first_number)
    e.delete(0,END)

def button_multi():
    first_number = e.get()
    global first_num
    global math
    math = "multiplication"
    first_num = int(first_number)
    e.delete(0,END)

def button_quo():
    first_number = e.get()
    global first_num
    global math
    math = "division"
    first_num = int(first_number)
    e.delete(0,END)

# define buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda:button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda:button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda:button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda:button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda:button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda:button_click(6))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda:button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda:button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda:button_click(0))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda:button_click(7))
button_equal = Button(root, text="=", padx=40, pady=20, command=button_equ)
button_clear = Button(root, text="clear", padx=29, pady=20, command=button_clean)
button_plus = Button(root, text="+", padx=40, pady=20, command=button_add)
button_subt = Button(root, text="-", padx=40, pady=20, command=button_diff)
button_pro = Button(root, text="*", padx=40, pady=20,command=button_multi)
button_div = Button(root, text="/", padx=40, pady=20, command=button_quo)

# put buttons on screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_plus.grid(row=3,column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_subt.grid(row=2,column=3)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_pro.grid(row=1,column=3)

button_0.grid(row=4, column=0)
button_equal.grid(row=4,column=1)
button_clear.grid(row=4,column=2)
button_div.grid(row=4,column=3)

root.mainloop()
