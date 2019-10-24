import tkinter
import tkinter.messagebox
import cv2
import PIL.Image, PIL.ImageTk


# https://solarianprogrammer.com/2018/04/20/python-opencv-show-image-tkinter-window/


# Callback for the "Blur" button
def blur_image():
    global photo
    global cv_img

    cv_img = cv2.blur(cv_img, (3, 3))
    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
    canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
    # canvas2.create_image(0, 0, image=photo, anchor=tkinter.NW)

    print("blurred")


def about_method():
    tkinter.messagebox.showinfo(title="Welcome", message="Run App!\n")


def exit_method():
    exit()


def print_hello():
    global photo
    global cv_img

    # cv_img = cv2.blur(cv_img, (3, 3))

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv_img = cv2.putText(img=cv_img,
                         text='OpenCV',
                         org=(100, 200),
                         fontFace=font,
                         fontScale=4,
                         color=(255, 255, 255),
                         thickness=2,
                         lineType=cv2.LINE_AA)
    # cv2.imshow('black_image_with_text', cv_img)
    # cv2.waitKey(0)
    #
    # cv2.destroyAllWindows()

    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
    canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)

    print("Hello!")


def reset_image():
    global photo
    global cv_img
    global cv_image_initial

    cv_img = cv_image_initial
    # photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
    photo = photo_initial
    canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
    # canvas2.create_image(0, 0, image=photo, anchor=tkinter.NW)
    isImageInitialObtained = False
    print("reset")


# mouse callback function
def draw_circle(event, x, y, flags, param):
    global photo
    global cv_img
    global cv_image_initial
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(cv_img, (x, y), 100, (255, 0, 0), -1)


def buttonPressed(event):
    # global photo
    # global cv_img
    mousePosition.set("Pressed at [ " + str(event.x) +
                      ", " + str(event.y) + " ]")
    cv2.circle(cv_img, (event.x, event.y), 100, (255, 0, 0), -1)

    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
    canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)


# Create a window
window = tkinter.Tk()
window.title("OpenCV and Tkinter")
window.geometry("1400x700")

#####################
mousePosition = tkinter.StringVar()  # displays mouse position
mousePosition.set("Mouse outside window")

positionLabel = tkinter.Label(textvariable=mousePosition)
positionLabel.pack(side=tkinter.BOTTOM)
# bind mouse events to window
window.bind(sequence="<Button-1>", func=buttonPressed)
#####################


# Load an image using OpenCV
cv_img = cv2.cvtColor(cv2.imread("./img1.jpg"), cv2.COLOR_BGR2RGB)
cv_img = cv2.resize(cv_img, None, fx=0.32, fy=0.32)
# cv2.setMouseCallback('OpenCV and Tkinter', draw_circle)

isImageInitialObtained = False
if isImageInitialObtained == False:
    cv_image_initial = cv_img.copy()
    isImageInitialObtained = True

# Get the image dimensions (OpenCV stores image data as NumPy ndarray)
height, width, no_channels = cv_img.shape

# Create a canvas that can fit the above image
canvas = tkinter.Canvas(master=window, width=width, height=height)
canvas2 = tkinter.Canvas(master=window, width=width, height=height)
# canvas.pack()
canvas.place(x=10, y=10)
canvas2.place(x=700, y=10)

# Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
photo_initial = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_image_initial))

# Add a PhotoImage to the Canvas
canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
canvas2.create_image(0, 0, image=photo_initial, anchor=tkinter.NW)

# Button that lets the user blur the image
btn_run = tkinter.Button(window, text="Run", width=5, command=print_hello)
btn_run.place(x=10, y=600)

# Button that lets the user blur the image
btn_reset = tkinter.Button(window, text="Reset", width=5, command=reset_image)
btn_reset.place(x=150, y=600)

# Button that lets the user blur the image
btn_blur = tkinter.Button(window, text="Blur", width=5, command=blur_image)
btn_blur.place(x=300, y=600)

# Button that lets the user blur the image
btn_exit = tkinter.Button(window, text="Exit", width=5, command=exit_method)
btn_exit.place(x=600, y=600)

# Run the window loop
window.mainloop()
