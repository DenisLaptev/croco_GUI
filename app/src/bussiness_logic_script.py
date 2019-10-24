import numpy as np
import cv2
import matplotlib.pyplot as plt

import tkinter
import tkinter.messagebox

import PIL.Image, PIL.ImageTk



PATH_TO_FOLDER_IMAGE_INITIAL = '../resources/images_initial/'
PATH_TO_FOLDER_IMAGE_GROUND_TRUTH = '../resources/images_photoshop/'
PATH_TO_FOLDER_FILE_CSV = '../resources/csv/'
PATH_TO_FOLDER_FILE_PKL = 'r../resources/pkl/'

def make_modified_image(src_image):
    src_image_copy=src_image.copy()
    result_image = cv2.ellipse(src_image_copy, (256, 256), (100, 50), 0, 0, 360, 255, -1)

    cv2.imshow('result_image', result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return result_image

def get_GT_image(image_number):
    if image_number == 1:
        FILE_NAME_IMAGE_INITIAL = 'img1.jpg'
        FILE_NAME_IMAGE_GROUND_TRUTH = 'cells1.jpg'
        FILE_NAME_FILE_CSV = 'csv1.txt'
        FILE_NAME_FILE_PKL = ''
    elif image_number == 2:
        FILE_NAME_IMAGE_INITIAL = 'img2_2016-03-01 21.42.11.jpg'
        FILE_NAME_IMAGE_GROUND_TRUTH = 'cells2_2016-03-01 21.42.11.jpg'
        FILE_NAME_FILE_CSV = 'csv2.txt'
        FILE_NAME_FILE_PKL = 'cells1.pkl'
    elif image_number == 3:
        FILE_NAME_IMAGE_INITIAL = 'img3_20160630_160547.jpg'
        FILE_NAME_IMAGE_GROUND_TRUTH = 'cells3_20160630_160547.jpg'
        FILE_NAME_FILE_CSV = 'csv3.txt'
        FILE_NAME_FILE_PKL = 'cells2_2016-03-01_21.42.11.pkl'
    elif image_number == 4:
        FILE_NAME_IMAGE_INITIAL = 'img4_20160630_160548.jpg'
        FILE_NAME_IMAGE_GROUND_TRUTH = 'cells4_20160630_160548.jpg'
        FILE_NAME_FILE_CSV = 'csv4.txt'
        FILE_NAME_FILE_PKL = 'cells4_20160630_160548.pkl'
    elif image_number == 5:
        FILE_NAME_IMAGE_INITIAL = 'img5_croc82.jpg'
        FILE_NAME_IMAGE_GROUND_TRUTH = 'cells5_croc82_GT.png'
        FILE_NAME_FILE_CSV = 'csv1.txt'
        FILE_NAME_FILE_PKL = 'cells4_20160630_160548.pkl'
    else:
        print('INCORRECT NUMBER!')



    PATH_TO_IMAGE_INITIAL = PATH_TO_FOLDER_IMAGE_INITIAL + FILE_NAME_IMAGE_INITIAL
    PATH_TO_IMAGE_GROUND_TRUTH = PATH_TO_FOLDER_IMAGE_GROUND_TRUTH + FILE_NAME_IMAGE_GROUND_TRUTH
    PATH_TO_FILE_CSV = PATH_TO_FOLDER_FILE_CSV + FILE_NAME_FILE_CSV
    PATH_TO_FILE_PKL = PATH_TO_FOLDER_FILE_PKL + FILE_NAME_FILE_PKL

    GT_image = cv2.imread(PATH_TO_IMAGE_GROUND_TRUTH)

    return GT_image
