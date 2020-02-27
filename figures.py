import tkinter as tk
from tkinter import colorchooser
from random import randint
import threading
import time

flag = True
color = 'green'


root = tk.Tk()
root.geometry('1000x650')
root.resizable(0, 0)
root.config(bg='#ccc')
canvas = tk.Canvas(width=1000, height=600)
canvas.pack()


def get_color():
    global color
    color = colorchooser.askcolor()[1]


def clean():
    canvas.delete('all')


def stop():
    global flag
    flag = False


def random_move():
    while True:
        if flag:
            time.sleep(.3)
            x, y = randint(25, 975), randint(25, 575)
            x1 = randint(0, 3)
            h = x + 25
            z = y + 25
            if x1 == 0:
                canvas.create_oval(x, y, h, z, fill=color)
            elif x1 == 1:
                canvas.create_rectangle(x, y, h, z, fill=color)
            else:
                coords = [(x, y), (h - 10, z + 10), (h + 15, z - 15)]
                canvas.create_polygon(coords, fill=color, outline="#000")
        else:
            break


def start():
    global flag
    flag = True
    t1 = threading.Thread(target=random_move)
    t1.start()


b1 = tk.Button(root, text='Start', command=start)
b1.pack(side='left', padx=2)
b2 = tk.Button(root, text='Stop', command=stop)
b2.pack(side='left', padx=2)
b3 = tk.Button(root, text='Clean', command=clean)
b3.pack(side='left', padx=2)
b4 = tk.Button(root, text='Color', command=get_color)
b4.pack(side='left', padx=2)


root.mainloop()
