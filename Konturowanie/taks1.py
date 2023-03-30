import cv2 as cv
import numpy as np

img = cv.imread("../images/not_bad.jpg", cv.IMREAD_GRAYSCALE)
img_color = cv.imread("../images/not_bad.jpg", cv.IMREAD_COLOR)
img = cv.resize(img, dsize=(512, 512))
img_color = cv.resize(img_color, dsize=(512, 512))
img_color_ = img_color.copy()
dstPts = np.array([[img.shape[0], img.shape[1]], [0, img.shape[1]], [img.shape[0], 0], [0, 0]], np.float32)


def show(img):
    cv.imshow("img", img)
    cv.waitKey(2000)


img = cv.medianBlur(img, 5)
ret, thresh = cv.threshold(img, 60, 255, cv.THRESH_BINARY_INV)
kernel = np.ones((5, 5), np.uint8)
erosion = cv.erode(thresh, kernel, iterations=1)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
img_contours = cv.drawContours(img_color_, contours, -1, (0, 255, 0), thickness=2)

Moments = []
centroids = []
for c in contours:
    M = cv.moments(c)
    Moments.append(M)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    centroids.append((cx, cy))

srcPts = np.array(centroids, np.float32)
transform = cv.getPerspectiveTransform(srcPts, dstPts)
dst = cv.warpPerspective(img_color_, transform, (img.shape[0], img.shape[1]))
show(dst)
