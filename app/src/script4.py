import tkinter
import cv2
import PIL.Image, PIL.ImageTk


# Callback for the "Blur" button
def blur_image():
    global photo
    global cv_img

    cv_img = cv2.blur(cv_img, (3, 3))
    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
    canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)

    print("blurred")

def print_hello():
    global photo
    global cv_img

    #cv_img = cv2.blur(cv_img, (3, 3))

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv_img = cv2.putText(img=cv_img,
                         text='OpenCV',
                         org=(10, 500),
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

    print("blurred")


# Create a window
window = tkinter.Tk()
window.title("OpenCV and Tkinter")
window.geometry("1300x700")

# Load an image using OpenCV
cv_img = cv2.cvtColor(cv2.imread("./mainlogo.png"), cv2.COLOR_BGR2RGB)

# Get the image dimensions (OpenCV stores image data as NumPy ndarray)
height, width, no_channels = cv_img.shape

# Create a canvas that can fit the above image
canvas = tkinter.Canvas(window, width=width, height=height)
canvas.pack()

# Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))

# Add a PhotoImage to the Canvas
canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)

# Button that lets the user blur the image
#btn_blur = tkinter.Button(window, text="Blur", width=50, command=blur_image)
btn_blur = tkinter.Button(window, text="Blur", width=50, command=print_hello)
btn_blur.pack(anchor=tkinter.CENTER, expand=True)

# Run the window loop
window.mainloop()
