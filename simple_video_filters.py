from tkinter import Button, Canvas, Frame, Tk
import cv2
import numpy as np
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk


class Application(Frame):
    def __init__(self, root):
        super(Application, self).__init__(root)
        self.root = root
        self.delay = 15
        self.canwidth = 850
        self.canhight = 450
        self.pause = False
        self.gray = False

        # ---------Filters----------
        self.btn1 = Button(text='Gray',
                           fg='white',
                           bg='black',
                           padx='20',
                           pady='10',
                           command=lambda: self.reverve_value('gray'))
        self.btn1.place(x='50', y='50')

        # ----------Video-------------
        self.btn_open = Button(text='Open file',
                               fg='white',
                               bg='black',
                               padx='20',
                               pady='10',
                               command=self.video)
        self.btn_open.place(x='200', y='480')
        self.btn_pause = Button(text='Pause',
                                fg='white',
                                bg='black',
                                padx='20',
                                pady='10',
                                command=self.pause_video)
        self.btn_pause.place(x='310', y='480')

        # ------------Canvas---------------
        self.canvas = Canvas(root, width=850, height=450, bg='blue')
        self.canvas.place(x='200', y='1')

    def reverve_value(self, x):
        setattr(self, x, not getattr(self, x))

    def start_video(self):
        self.ret, self.frame = self.vid.read()
        if self.ret:
            if self.gray:
                self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
            else:
                self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)

            self.frame = cv2.resize(self.frame, (self.canwidth, self.canhight))
            self.photo = ImageTk.PhotoImage(
                image=Image.fromarray(self.frame)
            )
            self.canvas.create_image(1, 1, image=self.photo, anchor="nw")
        else:
            self.btn_open.config(state="normal")
            self.pause = True
        if not self.pause:
            self.root.after(self.delay, self.start_video)

    def pause_video(self):
        if self.pause is False:
            self.pause = True
            self.btn_open.config(state="normal")
        else:
            self.pause = False
            self.btn_open.config(state="disabled")
            self.start_video()

    def open_file(self):
        fopen = askopenfile(mode='rb',
                            defaultextension=".mp4",
                            filetypes=(
                                ("Video files", ".mp4"),
                                ("All files", ".*")
                            ))
        if fopen:
            self.vid = cv2.VideoCapture(fopen.name)

    def video(self):
        self.pause = False
        self.open_file()
        self.btn_open.config(state="disabled")
        self.start_video()


root = Tk()
root.title("Simple video filters")
root.geometry('1100x550')
root.resizable(False, False)
app = Application(root)
root.mainloop()
