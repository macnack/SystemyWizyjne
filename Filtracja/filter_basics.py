import cv2 as cv
import numpy as np

path_noise = "../images/lenna_salt_and_pepper.bmp"
path_salt_and_pepper = "../images/lenna_noise.bmp"

noise = cv.imread(path_noise, cv.IMREAD_COLOR)
salt_and_pepper = cv.imread(path_salt_and_pepper, cv.IMREAD_COLOR)

img = salt_and_pepper

def filter_callback(value):
    cv.imshow("Orginal Image",  img)
    if (value % 2 == 1) and (value > 3):
        cv.imshow("Median Blur", cv.medianBlur(noise, value))
        cv.imshow("Blur", cv.blur(img, ksize=(value, value)))
        cv.imshow("Gaussian Blur", cv.GaussianBlur(noise, sigmaX= cv.BORDER_DEFAULT, ksize=(value, value)))

def show():
    cv.namedWindow('Filtering')
    cv.createTrackbar('size', 'Filtering', 0, 100, filter_callback)

if __name__ == '__main__':
    while True:
        cv.namedWindow('Filtering')
        cv.createTrackbar('size', 'Filtering', 0, 100, filter_callback)
        key = cv.waitKey(10)
        if key == 27:
            cv.destroyAllWindows()

