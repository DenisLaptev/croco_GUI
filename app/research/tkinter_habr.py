import tkinter as tk
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import cv2


tk._test()

root = Tk()


def Hello(event):
    print("Yet another hello world")
    image = cv2.imread('./mainlogo.png')
    cv2.imshow('image',image)
    k = cv2.waitKey(0)
    # wait for ESC key to exit
    if k == 27:
        cv2.destroyAllWindows()


btn = Button(root,                    # родительское окно
             text="Click me",         # надпись на кнопке
             width=30, height=5,      # ширина и высота
             bg="white", fg="black")  # цвет фона и надписи
btn.bind("<Button-1>", Hello)         # при нажатии ЛКМ на кнопку вызывается функция Hello
btn.pack()                            # расположить кнопку на главном окне
root.mainloop()
