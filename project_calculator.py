from tkinter import *

root = Tk()
root.title("Calculator")
root.resizable(0, 0)
root.configure(bg="black")


def button_clicked(number):
    e.insert(END, number)


def equals_clicked():
    exp = e.get()
    if exp == "":
        e.insert(0, "")
    elif exp[0] == "0":
        exp = exp[1:]
        calculate(exp)
    else:
        calculate(exp)


def clear_clicked():
    e.delete(0, END)


def calculate(exp):
    res = eval(exp)
    e.delete(0, END)
    e.insert(0, res)

eqhei =50

e = Entry(width=28, borderwidth=5, font=20, bg="black", fg="white")
e.grid(row=0, column=0, columnspan=4)

b1 = Button(root, bg="black", fg="white", text="1", padx=35, pady=20, command=lambda: button_clicked(1))
b2 = Button(root, bg="black", fg="white", text="2", padx=35, pady=20, command=lambda: button_clicked(2))
b3 = Button(root, bg="black", fg="white", text="3", padx=35, pady=20, command=lambda: button_clicked(3))
b4 = Button(root, bg="black", fg="white", text="4", padx=35, pady=20, command=lambda: button_clicked(4))
b5 = Button(root, bg="black", fg="white", text="5", padx=35, pady=20, command=lambda: button_clicked(5))
b6 = Button(root, bg="black", fg="white", text="6", padx=35, pady=20, command=lambda: button_clicked(6))
b7 = Button(root, bg="black", fg="white", text="7", padx=35, pady=20, command=lambda: button_clicked(7))
b8 = Button(root, bg="black", fg="white", text="8", padx=35, pady=20, command=lambda: button_clicked(8))
b9 = Button(root, bg="black", fg="white", text="9", padx=35, pady=20, command=lambda: button_clicked(9))
b0 = Button(root, bg="black", fg="white", text="0", padx=35, pady=20, command=lambda: button_clicked(0))

b_add = Button(root, bg="black", fg="white", text="+", padx=35, pady=20, command=lambda: button_clicked("+"))
b_sub = Button(root, bg="black", fg="white", text="-", padx=35, pady=20, command=lambda: button_clicked("-"))
b_mul = Button(root, bg="black", fg="white", text="*", padx=35, pady=20, command=lambda: button_clicked("*"))
b_div = Button(root, bg="black", fg="white", text="/", padx=35, pady=20, command=lambda: button_clicked("/"))

b_equals = Button(root, bg="black", fg="white", text="=", padx=35, pady=20, command=equals_clicked)
b_clear = Button(root, bg="black", fg="white", text="C", padx=35, pady=20, command=clear_clicked)

b7.grid(row=3, column=0)
b8.grid(row=3, column=1)
b9.grid(row=3, column=2)
b_add.grid(row=3, column=3)

b4.grid(row=4, column=0)
b5.grid(row=4, column=1)
b6.grid(row=4, column=2)
b_sub.grid(row=4, column=3)

b1.grid(row=5, column=0)
b2.grid(row=5, column=1)
b3.grid(row=5, column=2)
b_mul.grid(row=5, column=3)

b_clear.grid(row=6, column=0)
b0.grid(row=6, column=1)
b_div.grid(row=6, column=2)
b_equals.grid(row=6, column=3)

root.mainloop()
