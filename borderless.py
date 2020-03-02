import tkinter as tk
root = tk.Tk()

root.image = tk.PhotoImage(file='images/ship.gif')
label = tk.Label(root, image=root.image, bg='white')
root.overrideredirect(True)
root.geometry("+250+250")
root.lift()
root.wm_attributes("-topmost", True)
root.wm_attributes("-transparentcolor", "white")

xwin = -50
ywin = -50


def get_pos(event):
    xwin = root.winfo_x()
    ywin = root.winfo_y()
    startx = event.x_root
    starty = event.y_root

    ywin = ywin - starty
    xwin = xwin - startx


def move_window(event):
    root.geometry('+{0}+{1}'.format(event.x_root + xwin, event.y_root + ywin))


label.bind('<B1-Motion>', move_window)
label.bind('<Button-1>', get_pos)

label.pack()
label.mainloop()
