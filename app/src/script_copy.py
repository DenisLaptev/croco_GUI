import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog
from tkinter import *
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk  # pip install pillow


def exit_method():
    exit()


def about_method():
    tkinter.messagebox.showinfo(title="Welcome", message="This is some info about the project!")


def LoadFile(ev):
    fn = filedialog.Open(root).show()
    if fn == '':
        return
    return fn
    # textbox.delete('1.0', 'end')
    # textbox.insert('1.0', open(fn, 'rt').read())

def SaveFile(ev):
    fn = filedialog.SaveAs(root, filetypes=[('.jpg', '.jpeg','.png')]).show()
    # if fn == '':
    #     return
    # if not fn.endswith(".txt"):
    #     fn += ".txt"
    #open(fn, 'wt').write(textbox.get('1.0', 'end'))

def Quit(ev):
    global root
    root.destroy()

def print_image():
    canvas = Canvas(root, width=300, height=300)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open("ball.png"))
    canvas.create_image(20, 20, anchor=NW, image=img)


root = tk.Tk()
root.geometry("500x500")
root.title("Crocodiles GUI Util")


label_0 = tk.Label(master=root,
                   width=20,
                   text="Crocodiles GUI Util",
                   font=("arial", 19, "bold")
                   ).place(x=90, y=53)
button_1 = tk.Button(master=root,
                     fg="white",
                     bg="brown",
                     relief=tk.GROOVE,  # GROOVE, RIDGE, SUNKEN, RAISED
                     text="sign up",
                     width=8,
                     font=("arial", 16, "bold"),
                     command=about_method
                     )
button_1.place(x=40, y=420)

button_2 = tk.Button(master=root,
                     fg="white",
                     bg="brown",
                     relief=tk.GROOVE,  # GROOVE, RIDGE, SUNKEN, RAISED
                     text="exit",
                     width=8,
                     font=("arial", 16, "bold"),
                     command=exit_method
                     )
button_2.place(x=200, y=420)








panelFrame = Frame(root, height=60, bg='gray')
imageFrame = Frame(root, height=340, width=600)

panelFrame.pack(side='top', fill='x')
imageFrame.pack(side='bottom', fill='both', expand=1)

load = Image.open("../research/mainlogo.png")
load = Image.open("../research/mainlogo.png")
render = ImageTk.PhotoImage(load)

imagebox = Label(root, image=render)
scrollbar = Scrollbar(imageFrame)

#scrollbar['command'] = imagebox.yview
#imagebox['yscrollcommand'] = scrollbar.set

imagebox.pack(side='left', fill='both', expand=1)
scrollbar.pack(side='right', fill='y')

loadBtn = Button(panelFrame, text='Load')
saveBtn = Button(panelFrame, text='Save')
quitBtn = Button(panelFrame, text='Quit')

loadBtn.bind("<Button-1>", LoadFile)
saveBtn.bind("<Button-1>", SaveFile)
quitBtn.bind("<Button-1>", Quit)

loadBtn.place(x=10, y=10, width=40, height=40)
saveBtn.place(x=60, y=10, width=40, height=40)
quitBtn.place(x=110, y=10, width=40, height=40)



root.mainloop()
