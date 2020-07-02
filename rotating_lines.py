import tkinter as tk
import math
import time
import threading


class Application(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.flag = False

        self.btn = tk.Button(root, text='Toggle rotate', command=self.toggle)
        self.btn.pack()

        self.canvas = tk.Canvas(root, width=500, height=250, bg="white")
        self.canvas.pack()

        self.angle = 0

    def toggle(self):
        self.flag = not self.flag
        if self.flag:
            threading.Thread(target=self.rotate).start()

    def rotate(self):
        while self.flag:
            self.canvas.delete('all')
            self.create_new_line(100, 100, 100, 2)
            self.create_new_line(350, 125, 125, 5, reverse=True)
            self.angle += 1
            time.sleep(0.01)

    def create_new_line(self, x1, y1, length, width, reverse=False):
        angle = math.radians(self.angle)
        if reverse:
            angle = - angle
        end_x = x1 + length * math.cos(angle)
        end_y = y1 + length * math.sin(angle)
        self.canvas.create_line(x1, y1, end_x, end_y, width=width)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Rotating lines')
    root.geometry('500x300+300+100')
    root.resizable(False, False)
    Application(root)
    root.mainloop()
