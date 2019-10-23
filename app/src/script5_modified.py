import tkinter
import tkinter.messagebox
import cv2
import PIL.Image, PIL.ImageTk

class App:
    def __init__(self, window, window_title, image_path="img1.jpg"):
        self.window = window
        self.window.title(window_title)
        self.window.geometry("1400x700")

        # Load an image using OpenCV
        self.cv_img = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
        self.cv_img = cv2.resize(self.cv_img, None, fx=0.25, fy=0.25)
        self.cv_img_copy = self.cv_img.copy()

        # Get the image dimensions (OpenCV stores image data as NumPy ndarray)
        self.height, self.width, no_channels = self.cv_img.shape

        # Create a canvas that can fit the above image
        self.canvas = tkinter.Canvas(master=window, width = self.width, height = self.height)
        self.canvas.place(x=10, y=10)

        self.canvas2 = tkinter.Canvas(master=window, width=self.width, height=self.height)
        self.canvas2.place(x=700, y=10)

        # Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))
        self.photo_initial = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img_copy))

        # Add a PhotoImage to the Canvas
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)
        self.canvas2.create_image(0, 0, image=self.photo_initial, anchor=tkinter.NW)

        # Button that lets the user blur the image
        self.btn_run=tkinter.Button(window, text="Run", width=10, command=self.run_method)
        self.btn_run.place(x=10, y=600)

        # Button that lets the user blur the image
        self.btn_blur = tkinter.Button(window, text="Blur", width=10, command=self.blur_image)
        self.btn_blur.place(x=300, y=600)

        # Button that lets the user blur the image
        self.btn_exit = tkinter.Button(window, text="Exit", width=10, command=self.exit_method)
        self.btn_exit.place(x=600, y=600)

        self.window.mainloop()

    # Callback for the "Blur" button
    def blur_image(self):
        self.cv_img = cv2.blur(self.cv_img, (3, 3))
        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

    def run_method(self):
        tkinter.messagebox.showinfo(title="Welcome", message="Run App!")

    def exit_method(self):
        exit()

    def print_hello(self):
        print('Hello Worlds!')


# Create a window and pass it to the Application object
App(tkinter.Tk(), "Tkinter and OpenCV", image_path="img2.jpg")