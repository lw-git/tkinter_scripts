from tkinter import Canvas, Button, Tk
from random import randint
import threading
import time

root = Tk()
root.geometry('1000x750')
root.resizable(0, 0)
root.config(bg='#ccc')
canvas = Canvas(width=1000, height=700)
canvas.pack()

balls = []
for i in range(20):
    x, y = randint(50, 950), randint(50, 650)
    h = x + 25
    z = y + 25
    balls.append(canvas.create_oval(x, y, h, z, width=5, fill='green'))

flag = False


def func(ball, dx, dy):
    global flag
    dx, dy = dx, dy
    while True:
        if flag:
            break
        time.sleep(.01)
        canvas.move(ball, dx, dy)
        canvas.update()

        if canvas.coords(ball)[0] > 975:
            dx = -dx
        elif canvas.coords(ball)[0] < 0:
            dx = -dx

        if canvas.coords(ball)[1] > 675:
            dy = -dy
        elif canvas.coords(ball)[1] < 0:
            dy = -dy


def start():
    global flag
    flag = False
    for ball in balls:
        t1 = threading.Thread(target=func, args=[ball, randint(-10, 10), randint(-10, 10)])
        t1.start()

def stop():
    global flag
    flag = True


button1 = Button(root, text='Start', command=start)
button1.pack(side='left', padx='5')

button2 = Button(root, text='Stop', command=stop)
button2.pack(side='left', padx='5')


root.mainloop()