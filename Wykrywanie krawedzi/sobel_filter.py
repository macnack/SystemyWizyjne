import numpy as np
import cv2 as cv
path = "../images/"
img = cv.imread(path + 'lenna_gray.png')
Mx = np.array([[1, 0, - 1], [2, 0, -2], [1, 0, -1]], np.int8)
My = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], np.int8)

def normalize8(I):
  mn = I.min()
  mx = I.max()

  mx -= mn

  I = ((I - mn)/mx) * 255
  return I.astype(np.uint8)
#s01e05
img_kx = cv.filter2D(img, ddepth=cv.CV_32F, kernel=Mx) / 4.0

img_ky = cv.filter2D(img, ddepth=cv.CV_32F, kernel=My) / 4.0

## Funkcja gradientu:
img_gradient = cv.sqrt(cv.pow(img_kx, 2) + cv.pow(img_ky, 2))
# Zamiana na uint8
img_gradient = img_gradient.astype(np.uint8)

# zdjecie moze zawierac wartosci ujemne zatem:
img_kx = abs(img_kx)
img_ky = abs(img_ky)
# Dokonujemy normalizacji...
img_kx = normalize8(img_kx)
img_ky = normalize8(img_ky)
cv.imshow('Img', img)
cv.waitKey(1000)
cv.imshow('kx', img_kx)
cv.waitKey(1000)
cv.imshow('ky', img_ky)
cv.waitKey(1000)
cv.imshow('Gradient', img_gradient.astype(np.uint8))
cv.waitKey(1000)
