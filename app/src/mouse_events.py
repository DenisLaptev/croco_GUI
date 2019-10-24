from tkinter import *


class MouseLocation(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Demonstrating Mouse Events")
        self.master.geometry("275x100")

        self.mousePosition = StringVar()  # displays mouse position
        self.mousePosition.set("Mouse outside window")
        self.positionLabel = Label(self,
                                   textvariable=self.mousePosition)
        self.positionLabel.pack(side=BOTTOM)

        # bind mouse events to window
        self.bind("<Button-1>", self.buttonPressed)

    def buttonPressed(self, event):
        self.mousePosition.set("Pressed at [ " + str(event.x) +
                               ", " + str(event.y) + " ]")


def main():
    MouseLocation().mainloop()


if __name__ == "__main__":
    main()