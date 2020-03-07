import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.attributes("-toolwindow", 1)
root.title("Tabs")
n = ttk.Notebook(root)
n.pack(fill='both', expand=True)
pages = []
for page in range(5):
    child = ttk.Frame(root)
    lab = ttk.Label(child, text='text %i' % page)
    lab.pack()
    n.add(child, text='page %i' % page)
    pages.append(child)

textForPage1 = tk.Text(pages[1])
textForPage1.pack(fill='both', expand=True)
root.mainloop()
