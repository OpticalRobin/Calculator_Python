from tkinter import *

def update_calc(press):
    global calculate
    calculate += press
    calc.config(text=calculate)

def calc_result():
    global result, calculate
    result = eval(calculate)
    results.config(text=result)
    calculate = ""

def back_char():
    global calculate
    calculate = calculate[:-1]
    calc.config(text=calculate)

def clear_screen():
    global calculate, result
    calculate = ""
    result = ""
    results.config(text=result)
    calc.config(text=calculate)

def close_window():
    calculate=""
    root.destroy()

def center_window(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width

    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2

    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

# function for updating the movement of the window
def move_window(event):
    root.geometry(f"+{event.x_root}+{event.y_root}")

root = Tk()
root.title("Calculator")
root.geometry("500x650")
root.config(bg="Black")
root.overrideredirect(True)

# creating a custom title bar using a frame.
# coloring it grey with a label and a close button
title_bar = Frame(root, bg="grey", relief="raised", bd=2)
title_label = Label(title_bar, text="Calculator", bg="grey", fg="white")
close_button = Button(title_bar, text="X", command=close_window, bg="grey", fg="white")

# packing the bar on the window
# and then packing the label and button onto the title bar
title_bar.pack(fill=X)
title_label.pack(side="left", padx=10)
close_button.pack(side="right", padx=5)

# Bind title bar motion to the move window function.
title_bar.bind("<B1-Motion>", move_window)

calculate = ""
result = ""

calc = Label(root, text=calculate, bg="grey", fg="white", height=5, borderwidth=2, relief="solid", font=40)
calc.pack(side="top", fill=X)

results = Label(root, text=result, bg="grey", fg="white", height=5, borderwidth=2, relief="solid", font=40)
results.pack(side="top", fill=X)

num_buttons = Frame(root, bg="black")
num_buttons.pack(side="bottom")

# / * -
button_div = Button(num_buttons, text="/", bg="grey", fg="white", height=3, width=10, command=lambda: update_calc("/"))
button_div.grid(row=0, column=0)

button_mul = Button(num_buttons, text="*", bg="grey", fg="white", height=3, width=10, command=lambda: update_calc("*"))
button_mul.grid(row=0, column=1)

button_sub = Button(num_buttons, text="-", bg="grey", fg="white", height=3, width=10, command=lambda: update_calc("-"))
button_sub.grid(row=0, column=2)

# numbers 1-3
button1 = Button(num_buttons, text="1", bg="grey", fg="white", height=3, width=10, command=lambda: update_calc("1"))
button1.grid(row=1, column=0)

button2 = Button(num_buttons, text="2", bg="grey", fg="white", height=3, width=10, command=lambda: update_calc("2"))
button2.grid(row=1, column=1)

button3 = Button(num_buttons, text="3", bg="grey", fg="white", height=3, width=10, command=lambda: update_calc("3"))
button3.grid(row=1, column=2)

# number 4-6
button4 = Button(num_buttons, text="4", bg="grey", fg="white", height=3, width=10, command=lambda: update_calc("4"))
button4.grid(row=2, column=0)

button5 = Button(num_buttons, text="5", bg="grey", fg="white", height=3, width=10, command=lambda: update_calc("5"))
button5.grid(row=2, column=1)

button6 = Button(num_buttons, text="6", bg="grey", fg="white", height=3, width=10, command=lambda: update_calc("6"))
button6.grid(row=2, column=2)

# numbers 7-9
button7 = Button(num_buttons, text="7", bg="grey", fg="white", height=3, width=10, command=lambda: update_calc("7"))
button7.grid(row=3, column=0)

button8 = Button(num_buttons, text="8", bg="grey", fg="white", height=3, width=10, command=lambda: update_calc("8"))
button8.grid(row=3, column=1)

button9 = Button(num_buttons, text="9", bg="grey", fg="white", height=3, width=10, command=lambda: update_calc("9"))
button9.grid(row=3, column=2)

# + 0 .
button_add = Button(num_buttons, text="+", bg="grey", fg="white", height=3, width=10, command=lambda: update_calc("+"))
button_add.grid(row=4, column=0)

button0 = Button(num_buttons, text="0", bg="grey", fg="white", height=3, width=10, command=lambda: update_calc("0"))
button0.grid(row=4, column=1)

button_dot = Button(num_buttons, text=".", bg="grey", fg="white", height=3, width=10, command=lambda: update_calc("."))
button_dot.grid(row=4, column=2)

# = button
button_eql = Button(num_buttons, text="=", bg="grey", fg="white", height=18, width=10, command=calc_result)
button_eql.grid(row=0, column=3, rowspan=5, sticky="ew")

button_del = Button(num_buttons, text="Back", bg="grey", fg="white", height=5, width=10, command=back_char)
button_del.grid(row=0, column=4, rowspan=2, sticky="ew")

button_cls = Button(num_buttons, text="Cls", bg="grey", fg="white", height=5, width=10, command=clear_screen)
button_cls.grid(row=3, column=4, rowspan=2, sticky="ew")

center_window(root)

root.mainloop()