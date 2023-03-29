import tkinter as tk
from tkinter import StringVar, Button, Entry
import tkinter.font as font

okno = tk.Tk()
okno.title("Calculator")

myFont = font.Font(family='Times New Roman', size=20, weight='bold')

expression = StringVar()
expression.set("")
ans_entry =  Entry(okno, textvariable=expression, bd=5, width=20, font=myFont, bg="gray", fg="white")
ans_entry.grid(row=0, column=0, columnspan=4)

def mouse_button_release(event):
    current = expression.get()
    if event.widget["text"] == "C":
        expression.set("")
    elif event.widget["text"] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        expression.set(current + event.widget["text"])
    elif event.widget["text"] in ["+", "-", "*", "/"]:
        expression.set(current + " " + event.widget["text"] + " ")
    elif event.widget["text"] == "=":
        try:
            result = eval(current)
            expression.set(result)
        except:
            expression.set("Error")

buttons = ["7", "8", "9", "/", "4", "5", "6", "*", "1", "2", "3", "-", "C", "0", "=", "+"]
row = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]
column = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]

for i in range(len(buttons)):
    button = Button(okno, text=buttons[i], width=4, height=2, font=myFont)
    button.grid(row=row[i], column=column[i])
    button.bind("<ButtonRelease-1>", mouse_button_release)

okno.mainloop()