import numpy as np
import cv2 as cv
path = "../images/"
img = cv.imread(path + 'lenna_gray.png')

def empty_callback(value):
    print("Trackbar reporting for duty with value: {}".format(value))
    pass

cv.namedWindow('Canny')
cv.createTrackbar('first threshold', 'Canny', 0, 100, empty_callback)
cv.createTrackbar('second threshold', 'Canny', 0, 100, empty_callback)
th1 = 25
th2 = 60
while True:
    canny = cv.Canny(img, threshold1=th1, threshold2=th2)
    cv.imshow('Canny', canny)

    th1 = cv.getTrackbarPos('first threshold', 'Canny')
    th2 = cv.getTrackbarPos('second threshold', 'Canny')
    key = cv.waitKey(10)
    if key == 27:
        cv.destroyAllWindows()

