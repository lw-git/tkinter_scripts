import tkinter as tk


def addItem():
    lbox.insert(tk.END, entry.get())
    entry.delete(0, tk.END)


def delList():
    select = list(lbox.curselection())
    select.reverse()
    for i in select:
        lbox.delete(i)


def saveList():
    with open('list.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lbox.get(0, tk.END)))


def loadList():
    try:
        with open('list.txt', 'r', encoding='utf-8') as f:
            for i in f:
                if i != '' and i != '\n':
                    lbox.insert(tk.END, i)
    except IOError:
        pass


root = tk.Tk()
root.title('TODO List')
root.after(200, loadList)
lbox = tk.Listbox(selectmode=tk.EXTENDED)
lbox.pack(side=tk.LEFT)
scroll = tk.Scrollbar(command=lbox.yview)
scroll.pack(side=tk.LEFT, fill=tk.Y)
lbox.config(yscrollcommand=scroll.set)

f = tk.Frame()
f.pack(side=tk.LEFT, padx=10)
entry = tk.Entry(f)
entry.pack(anchor=tk.N)
badd = tk.Button(f, text='Add', command=addItem)
badd.pack()
bdel = tk.Button(f, text='Delete', command=delList)
bdel.pack()
bsave = tk.Button(f, text='Save', command=saveList)
bsave.pack()

root.mainloop()
