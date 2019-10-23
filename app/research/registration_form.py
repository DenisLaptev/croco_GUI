import tkinter as tk
import tkinter.messagebox
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk  # pip install pillow
import sqlite3


fn_var = tk.StringVar()
ln_var = tk.StringVar()
dob_var = tk.StringVar()
country_var = tk.StringVar()

chbtn_1_var = "Java"
chbtn_2_var = "Python"

rbtn_var = tk.StringVar()

def exit1():
    exit()


def about_method():
    tkinter.messagebox.showinfo(title="Welcome", message="This is demo for About!")


def second_window():
    window2 = tk.Tk()
    window2.geometry("250x200")
    window2.title("Welcome to second window")
    label_nw = tk.Label(master=window2,
                        text="Registration Completed!",
                        relief="solid",
                        font=("arial", 10, "bold")).place(x=30, y=70)
    btn_nw = tk.Button(master=window2,
                       fg="white",
                       bg="brown",
                       relief=tk.GROOVE,  # GROOVE, RIDGE, SUNKEN, RAISED
                       text="button",
                       width=8,
                       font=("arial", 16, "bold"),
                       command=about_method
                       ).place(x=100, y=150)

def database():
    fname1=fn_var.get()
    lname1=ln_var.get()
    dob1=dob_var.get()
    country1 = country_var.get()
    prog_lang1=chbtn_2_var
    gender1= rbtn_var.get()

    conn = sqlite3.connect("Form_db")
    with conn:
        cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS students (fisrstName TEXT, lastName TEXT, dob TEXT, country TEXT, progLang TEXT, gender TEXT")
    


window = tk.Tk()
window.geometry("500x500")
window.title("Registration Form")

image = Image.open('./mainlogo.png')
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo).pack()

menu = tk.Menu(master=window)
window.config(menu=menu)

submenu_1 = tk.Menu(master=menu)
menu.add_cascade(label="File", menu=submenu_1)
submenu_1.add_command(label="Exit", command=exit1)

submenu_2 = tk.Menu(master=menu)
menu.add_cascade(label="Options", menu=submenu_2)
submenu_2.add_command(label="About", command=about_method)


def printt():
    print("Demo tkinter")
    print("fn_var =", fn_var)
    print("ln_var =", ln_var)

    fn = fn_var.get()
    ln = ln_var.get()
    dob = dob_var.get()
    country = country_var.get()
    gender = rbtn_var.get()

    print("fn =", fn)
    print("ln =", ln)
    print("dob =", dob)
    print("country =", country)
    print("gender =", gender)

    tkinter.messagebox.showinfo(title="welcome", message="User is successfully signed up!")

    # image = cv2.imread('./mainlogo.png')
    # cv2.imshow('image', image)
    # k = cv2.waitKey(0)
    # # wait for ESC key to exit
    # if k == 27:
    #     cv2.destroyAllWindows()


label_0 = tk.Label(window,
                   width=20,
                   text="Registration Form",
                   font=("arial", 19, "bold")
                   ).place(x=90, y=53)

label_1 = tk.Label(window,
                   width=20,
                   text="FirstName :",
                   font=("arial", 10, "bold")
                   ).place(x=80, y=130)

entry_1 = tk.Entry(window, textvar=fn_var)
entry_1.place(x=240, y=130)

label_2 = tk.Label(window,
                   width=20,
                   text="LastName :",
                   font=("arial", 10, "bold")
                   ).place(x=80, y=180)

entry_2 = tk.Entry(window, textvar=ln_var)
entry_2.place(x=240, y=180)

label_3 = tk.Label(window,
                   width=20,
                   text="DOB :",
                   font=("arial", 10, "bold")
                   ).place(x=80, y=230)

entry_3 = tk.Entry(window, textvar=dob_var)
entry_3.place(x=240, y=230)

label_4 = tk.Label(window,
                   width=20,
                   text="Country :",
                   font=("arial", 10, "bold")
                   ).place(x=80, y=280)

list_of_countries = ['Nepal', 'India', 'Canada']
dropDownList = tk.OptionMenu(window, country_var, *list_of_countries)
country_var.set('select country')
dropDownList.config(width=15)
dropDownList.place(x=240, y=280)

# entry_4 = tk.Entry(window, textvar=dob)
# entry_4.place(x=240, y=280)


label_4 = tk.Label(window,
                   width=20,
                   text="Prog Lang :",
                   font=("arial", 10, "bold")
                   ).place(x=80, y=320)

chbtn_1 = tk.Checkbutton(master=window, text="Java", variable=chbtn_1_var).place(x=240, y=320)
chbtn_2 = tk.Checkbutton(master=window, text="Python", variable=chbtn_2_var).place(x=300, y=320)

label_5 = tk.Label(window,
                   width=20,
                   text="Gender :",
                   font=("arial", 10, "bold")
                   ).place(x=80, y=370)

rbtn_1 = tk.Radiobutton(master=window, text="Male", variable=rbtn_var, value="Male").place(x=240, y=370)
rbtn_2 = tk.Radiobutton(master=window, text="Female", variable=rbtn_var, value="Female").place(x=300, y=370)

button_1 = tk.Button(window,
                     fg="white",
                     bg="brown",
                     relief=tk.GROOVE,  # GROOVE, RIDGE, SUNKEN, RAISED
                     text="sign up",
                     width=8,
                     font=("arial", 16, "bold"),
                     command=printt
                     )
button_1.place(x=40, y=420)

button_2 = tk.Button(window,
                     fg="white",
                     bg="brown",
                     relief=tk.GROOVE,  # GROOVE, RIDGE, SUNKEN, RAISED
                     text="exit",
                     width=8,
                     font=("arial", 16, "bold"),
                     command=exit1
                     )
button_2.place(x=200, y=420)

button_3 = tk.Button(window,
                     fg="white",
                     bg="brown",
                     relief=tk.GROOVE,  # GROOVE, RIDGE, SUNKEN, RAISED
                     text="login",
                     width=8,
                     font=("arial", 16, "bold"),
                     command=second_window
                     )
button_3.place(x=360, y=420)

window.mainloop()
