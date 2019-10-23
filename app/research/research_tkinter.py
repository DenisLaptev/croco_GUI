import tkinter as tk

window = tk.Tk()
window.geometry("300x300")
window.title("Welcome")

label_1 = tk.Label(window,
                   fg="blue",
                   bg="yellow",
                   relief="solid",
                   text="Welcome to tkinter",
                   font=("arial", 16, "bold")
                   ).place(x=50, y=110)

label_2 = tk.Label(window,
                   fg="blue",
                   bg="yellow",
                   text="Second label",
                   font=("arial", 16, "bold")
                   )
label_2.pack(fill=tk.BOTH, pady=2, padx=2)

button_1 = tk.Button(window,
                     fg="white",
                     bg="brown",
                     relief=tk.GROOVE,#GROOVE, RIDGE, SUNKEN, RAISED
                     #relief=tk.RIDGE,
                     #relief=tk.SUNKEN,
                     #relief=tk.RAISED,
                     text="Demo",
                     font=("arial", 16, "bold")
                     )
button_1.place(x=70, y=70)

window.mainloop()
