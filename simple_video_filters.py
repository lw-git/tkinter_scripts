from tkinter import Button, Canvas, Frame, Tk
import cv2
import numpy as np
from tkinter.filedialog import askopenfile, asksaveasfilename
from PIL import Image, ImageTk, ImageGrab


class Application(Frame):
    def __init__(self, root):
        super(Application, self).__init__(root)
        self.root = root
        self.delay = 15
        self.canwidth = 850
        self.canhight = 450
        self.pause = False
        self.gray = False
        self.sobel = False
        self.rotate = False
        self.neg = False
        self.mosaic = False
        self.sharp = False
        self.kernel_sharpening = np.array([[-1,-1,-1], [-1, 9,-1], [-1,-1,-1]])        

        # ---------Filters----------
        self.btn1 = Button(text='Gray',
                           fg='white',
                           bg='black',
                           padx='20',
                           pady='10',
                           command=lambda: self.reverve_value('gray'))
        self.btn1.place(x='50', y='50')
        self.btn2 = Button(text='Sobel',
                           fg='white',
                           bg='black',
                           padx='20',
                           pady='10',
                           command=lambda: self.reverve_value('sobel'))
        self.btn2.place(x='50', y='120')
        self.btn3 = Button(text='Rotate',
                           fg='white',
                           bg='black',
                           padx='20',
                           pady='10',
                           command=lambda: self.reverve_value('rotate'))
        self.btn3.place(x='50', y='190')
        self.btn4 = Button(text='Negative',
                           fg='white',
                           bg='black',
                           padx='20',
                           pady='10',
                           command=lambda: self.reverve_value('neg'))
        self.btn4.place(x='50', y='260')
        self.btn5 = Button(text='Mosaic',
                           fg='white',
                           bg='black',
                           padx='20',
                           pady='10',
                           command=lambda: self.reverve_value('mosaic'))
        self.btn5.place(x='50', y='330')
        self.btn6 = Button(text='Sharp',
                           fg='white',
                           bg='black',
                           padx='20',
                           pady='10',
                           command=lambda: self.reverve_value('sharp'))
        self.btn6.place(x='50', y='400')        

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
        self.btn_save = Button(text='Save image',
                                fg='white',
                                bg='black',
                                padx='20',
                                pady='10',
                                command=self.save_image)
        self.btn_save.place(x='400', y='480')
        self.btn_save.config(state="disabled")

        # ------------Canvas---------------
        self.canvas = Canvas(root, width=850, height=450, bg='blue')
        self.canvas.place(x='200', y='1')

    def mosaic_filter(self, selected_image, nsize=30):
        rows, cols, _ = selected_image.shape
        dist = selected_image.copy()
        for y in range(0, rows, nsize):
            for x in range(0, cols, nsize):
                dist[y: y + nsize, x: x + nsize] = (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))
        return dist

    def reverve_value(self, x):
        setattr(self, x, not getattr(self, x))

    def start_video(self):
        self.ret, self.frame = self.vid.read()
        if self.ret:
            if self.gray:
                self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
                self.btn5.config(state='disabled')
            else:
                self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                self.btn5.config(state='normal')

            if self.sobel:
                self.frame = np.uint8(cv2.Laplacian(self.frame, cv2.CV_64F))

            if self.rotate:
                self.frame = cv2.flip(self.frame, 0)

            if self.neg:
                self.frame = cv2.bitwise_not(self.frame)

            if self.mosaic:
                self.frame = self.mosaic_filter(self.frame)
                self.btn1.config(state='disabled')
            else:
                self.btn1.config(state='normal')

            if self.sharp:
                self.frame = cv2.filter2D(self.frame, -1, self.kernel_sharpening)

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

    def save_image(self):
        x = self.canvas.winfo_rootx()
        y = self.canvas.winfo_rooty()
        x2 = x + self.canvas.winfo_width()
        y2 = y + self.canvas.winfo_height()
        filename = asksaveasfilename()
        ImageGrab.grab([x, y, x2, y2]).save(filename)

    def pause_video(self):
        if self.pause is False:
            self.pause = True
            self.btn_open.config(state="normal")
            self.btn_save.config(state="normal")
        else:
            self.pause = False
            self.btn_open.config(state="disabled")
            self.btn_save.config(state="disabled")
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
