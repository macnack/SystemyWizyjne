import cv2 as cv
import numpy as np

path_noise = "../images/lenna_salt_and_pepper.bmp"
path_salt_and_pepper = "../images/lenna_noise.bmp"

noise = cv.imread(path_noise, cv.IMREAD_COLOR)
salt_and_pepper = cv.imread(path_salt_and_pepper, cv.IMREAD_COLOR)
img = salt_and_pepper
img_grey = cv.cvtColor( salt_and_pepper, cv.COLOR_RGB2GRAY)
ret,th3 = cv.threshold(img_grey,127,255,cv.THRESH_BINARY)
kernel = np.ones((5,5), np.uint8)
erosion = cv.erode(th3, kernel, iterations=1)
dilation = cv.dilate(th3,kernel,iterations = 1)

def morfologic_callback(value):
    if (value % 2 == 1) and (value > 3):
        kernel = np.ones((value,value), np.uint8)
        erosion = cv.erode(th3, kernel, iterations=1)
        dilation = cv.dilate(th3,kernel,iterations = 1)
        opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
        closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
        cv.imshow('Binary Threshlod',th3)
        cv.imshow('Erode', erosion )
        cv.imshow('Dilate', dilation)
        cv.imshow('Opening', opening )
        cv.imshow('Closing', closing)

def show():
    cv.namedWindow('Morfologic')
    cv.createTrackbar('size', 'Morfologic', 0, 100, morfologic_callback)

if __name__ == '__main__':
    while True:
        show()
        key = cv.waitKey(10)
        if key == 27:
            cv.destroyAllWindows()


#Morphological dilation makes objects more visible and fills in small holes in objects. Lines appear thicker, and filled shapes appear larger.
#Morphological erosion removes floating pixels and thin lines so that only substantive objects remain. Remaining lines appear thinner and shapes appear smaller.
#Morphological opening is useful for removing small objects and thin lines from an image while preserving the shape and size of larger objects in the image.
#Morphological closing is useful for filling small holes in an image while preserving the shape and size of large holes and objects in the image.

