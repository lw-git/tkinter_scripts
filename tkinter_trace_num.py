import tkinter as tk

root = tk.Tk()
root.geometry('500x150+300+300')
root.title('Only digits allowed')
sv = tk.StringVar()


def callback(sv):
    if sv.get():
        if not sv.get()[-1].isdigit():
            sv.set(sv.get()[:-1])


sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))

l1 = tk.Label(root, text='Only digits allowed:', font=('Helvetica', 15))
l1.place(x=25, y=20)
e1 = tk.Entry(root, textvariable=sv, font=('Helvetica', 15, 'bold'))
e1.place(x=25, y=50, w=450, h=30)
root.mainloop()
