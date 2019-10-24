import tkinter
import tkinter.messagebox
import cv2
import PIL.Image, PIL.ImageTk

from bussiness_logic_script import *

# https://solarianprogrammer.com/2018/04/20/python-opencv-show-image-tkinter-window/

PATH_TO_IMAGE = "./img1.jpg"


# Callback for the "Blur" button
def blur_image_method():
    global photo
    global cv_img

    cv_img = cv2.blur(cv_img, (3, 3))
    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
    canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)

    print("blur_image_method")


def about_method():
    global draw_cnts
    global radius

    # imagecase = imagecase_var.get()
    radius = radius_var.get()
    draw_cnts = False
    if (draw_cnts_chbtn_var.get() == 0):
        draw_cnts = False
    elif (draw_cnts_chbtn_var.get() == 1):
        draw_cnts = True
    tkinter.messagebox.showinfo(title="Welcome",
                                message="Run App!\n" +
                                        "radius=" + str(radius) + "\n" +
                                        "draw_cnts=" + str(draw_cnts))


    print("about_method")


def exit_method():
    print("exit_method")
    exit()

def experiment_method():
    global photo
    global cv_img

    some_image = make_modified_image(cv_img)
    cv_img = some_image
    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
    canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)

    print("experiment_method")

def GT_image_method():
    global photo
    global cv_img

    some_image = get_GT_image(image_number=1)
    cv_img = some_image
    cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)

    # width = 350
    # height = 450
    dim = (width, height)
    # resize image
    cv_img = cv2.resize(cv_img, dim, interpolation=cv2.INTER_AREA)

    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
    canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)

    print("GT_image_method")


def reset_image_method():
    global photo
    global cv_img
    # global cv_image_initial

    cv_img = cv2.cvtColor(cv2.imread(PATH_TO_IMAGE), cv2.COLOR_BGR2RGB)
    cv_img = cv2.resize(cv_img, None, fx=0.32, fy=0.32)

    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))

    canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)

    print("reset_image_method")


def left_mouse_button_pressed_method(event):
    global photo
    global cv_img
    global draw_cnts
    global radius

    mousePosition.set("Pressed at [ " + str(event.x) +
                      ", " + str(event.y) + " ]")
    cv2.circle(cv_img, (event.x, event.y), 3, (255, 0, 0), -1)
    if draw_cnts_chbtn_var.get() == 1:
        cv2.circle(cv_img, (event.x, event.y), radius, (255, 0, 0), 2)

    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
    canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)


# Create a window
window = tkinter.Tk()
window.title("OpenCV and Tkinter")
window.geometry("1400x700")

# Create variables
radius_var = tkinter.IntVar()
draw_cnts_chbtn_var = tkinter.IntVar()

draw_cnts = False
radius = 1

#####################
mousePosition = tkinter.StringVar()  # displays mouse position
mousePosition.set("Mouse outside window")

positionLabel = tkinter.Label(textvariable=mousePosition)
positionLabel.pack(side=tkinter.BOTTOM)
#####################


label_title = tkinter.Label(master=window,
                            width=20,
                            text="Crocodiles GUI Util",
                            font=("arial", 19, "bold")
                            ).place(x=90, y=5)

# Load an image using OpenCV
cv_img = cv2.cvtColor(cv2.imread("./img1.jpg"), cv2.COLOR_BGR2RGB)
cv_img = cv2.resize(cv_img, None, fx=0.32, fy=0.32)

isImageInitialObtained = False
if isImageInitialObtained == False:
    cv_image_initial = cv_img.copy()
    isImageInitialObtained = True

# Get the image dimensions (OpenCV stores image data as NumPy ndarray)
height, width, channels = cv_img.shape

# Create a canvas that can fit the above image
canvas = tkinter.Canvas(master=window, width=width, height=height)
canvas2 = tkinter.Canvas(master=window, width=width, height=height)

canvas.place(x=10, y=10)
canvas2.place(x=700, y=10)

# bind mouse events to canvas
canvas.bind(sequence="<Button-1>", func=left_mouse_button_pressed_method)

# Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
photo_initial = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_image_initial))

# Add a PhotoImage to the Canvas
canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
canvas2.create_image(0, 0, image=photo_initial, anchor=tkinter.NW)

label_radius = tkinter.Label(master=window,
                             width=10,
                             text="Radius :",
                             font=("arial", 10, "bold")
                             ).place(x=80, y=380)

entry_radius = tkinter.Entry(master=window, textvar=radius_var)
entry_radius.place(x=240, y=380)

label_draw_cnts = tkinter.Label(master=window,
                                width=20,
                                text="Draw Contours :",
                                font=("arial", 10, "bold")
                                ).place(x=80, y=400)

draw_cnts_chbtn = tkinter.Checkbutton(master=window, text="Draw", variable=draw_cnts_chbtn_var).place(x=240, y=400)

# Button Run
btn_run = tkinter.Button(window, text="Run", width=5, command=about_method)
btn_run.place(x=50, y=600)

# Button Reset
btn_reset = tkinter.Button(window, text="Reset", width=5, command=reset_image_method)
btn_reset.place(x=100, y=600)

# Button Blur
btn_blur = tkinter.Button(window, text="Blur", width=5, command=blur_image_method)
btn_blur.place(x=150, y=600)

# Button Exit
btn_exit = tkinter.Button(window, text="Exit", width=5, command=exit_method)
btn_exit.place(x=200, y=600)

# Button Experiment
btn_experiment = tkinter.Button(window, text="Experiment", width=10, command=experiment_method)
btn_experiment.place(x=250, y=600)

# Button GT image
btn_experiment = tkinter.Button(window, text="GT", width=10, command=GT_image_method)
btn_experiment.place(x=300, y=600)

# Create menu
menu = tkinter.Menu(master=window)
window.config(menu=menu)

submenu_1 = tkinter.Menu(master=menu)
menu.add_cascade(label="File", menu=submenu_1)
submenu_1.add_command(label="Exit", command=exit_method)

submenu_2 = tkinter.Menu(master=menu)
menu.add_cascade(label="Options", menu=submenu_2)
submenu_2.add_command(label="About", command=about_method)

# Run the window loop
window.mainloop()
