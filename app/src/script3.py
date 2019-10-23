import tkinter as tk
import tkinter.messagebox
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk  # pip install pillow

root = tk.Tk()
root.geometry("600x600")
root.title("Crocodiles GUI Util")

imagecase_var = tk.StringVar()
radius_var = tk.StringVar()
draw_cnts_chbtn_var = tk.IntVar()



def exit_method():
    exit()


def about_method():
    imagecase = imagecase_var.get()
    radius = radius_var.get()
    draw_cnts = False
    if(draw_cnts_chbtn_var.get()==0):
        draw_cnts = False
    elif (draw_cnts_chbtn_var.get() == 1):
        draw_cnts = True

    image = Image.open('../research/mainlogo.png')
    photo = ImageTk.PhotoImage(image)
    label_image = tk.Label(image=photo).place(x=200, y=50)
    tkinter.messagebox.showinfo(title="Welcome", message="Run App!\n"+"imagecase=" + str(imagecase)+"\n"+"radius=" + str(radius)+"\n"+"draw_cnts=" + str(draw_cnts))

def run_method():
    image = Image.open('../research/mainlogo.png')
    photo = ImageTk.PhotoImage(image)
    label_image = tk.Label(image=photo).place(x=200, y=50)
    print('Run Method')

def main():


    label_title = tk.Label(master=root,
                           width=20,
                           text="Crocodiles GUI Util",
                           font=("arial", 19, "bold")
                           ).place(x=90, y=5)

    label_imagecase = tk.Label(master=root,
                       width=20,
                       text="ImageCase :",
                       font=("arial", 10, "bold")
                       ).place(x=80, y=280)

    list_of_images = ['image_1', 'image_2', 'image_3','image_4','image_5']
    dropDownList = tk.OptionMenu(root, imagecase_var, *list_of_images)
    imagecase_var.set('select image')
    dropDownList.config(width=15)
    dropDownList.place(x=240, y=280)



    label_radius = tk.Label(master=root,
                            width=20,
                            text="Radius :",
                            font=("arial", 10, "bold")
                            ).place(x=80, y=250)

    entry_radius = tk.Entry(master=root, textvar=radius_var)
    entry_radius.place(x=240, y=250)

    label_draw_cnts = tk.Label(master=root,
                       width=20,
                       text="Draw Contours :",
                       font=("arial", 10, "bold")
                       ).place(x=80, y=320)

    draw_cnts_chbtn = tk.Checkbutton(master=root, text="Draw", variable=draw_cnts_chbtn_var).place(x=240, y=320)




    menu = tk.Menu(master=root)
    root.config(menu=menu)

    submenu_1 = tk.Menu(master=menu)
    menu.add_cascade(label="File", menu=submenu_1)
    submenu_1.add_command(label="Exit", command=exit_method)

    submenu_2 = tk.Menu(master=menu)
    menu.add_cascade(label="Options", menu=submenu_2)
    submenu_2.add_command(label="About", command=about_method)

    button_run = tk.Button(master=root,
                           fg="white",
                           bg="green",
                           relief=tk.GROOVE,  # GROOVE, RIDGE, SUNKEN, RAISED
                           text="RUN",
                           width=8,
                           font=("arial", 16, "bold"),
                           command=run_method
                           )
    button_run.place(x=40, y=500)

    button_info = tk.Button(master=root,
                            fg="white",
                            bg="brown",
                            relief=tk.GROOVE,  # GROOVE, RIDGE, SUNKEN, RAISED
                            text="Info",
                            width=8,
                            font=("arial", 16, "bold"),
                            command=about_method
                            )
    button_info.place(x=200, y=500)

    button_exit = tk.Button(master=root,
                            fg="white",
                            bg="brown",
                            relief=tk.GROOVE,  # GROOVE, RIDGE, SUNKEN, RAISED
                            text="Exit",
                            width=8,
                            font=("arial", 16, "bold"),
                            command=exit_method
                            )
    button_exit.place(x=360, y=500)

    root.mainloop()


if __name__ == '__main__':
    main()
