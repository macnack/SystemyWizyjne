import cv2 as cv
import numpy as np
import time
path = "../images/lenna_noise.bmp"

img = cv.imread(path, cv.IMREAD_GRAYSCALE)

kernel_size = [-1, 0 ,1]
kernel_step = []

new_img = np.zeros( shape=img.shape, dtype=np.uint8)

def after_three_is_white(img):
    for idx_col in range(img.shape[1]):
        if not(idx_col % 3):
            img[:, idx_col] = 255
    return img

for row in kernel_size:
    for col in kernel_size:
        kernel_step.append((row, col))

img = after_three_is_white(img)

start = time.thread_time_ns()
for row in range(img.shape[0]):
    for col in range(img.shape[1]):
        sum_kernel = 0
        for u in kernel_step:
            if (row + u[0] > -1) and (row + u[0] < img.shape[0]) and \
                    (col + u[1] > -1) and (col + u[1] < img.shape[1]):
                sum_kernel += img[row+u[0], col+u[1]]
        new_img[row, col] = sum_kernel / 9
end = time.thread_time_ns()
print("Own filter elapsed time {:1.4f}ms".format((end-start)*10**(-6)))
start = time.thread_time_ns()
blur = cv.blur(img, (3,3), borderType=cv.BORDER_REFLECT)
end = time.thread_time_ns()
print("Blur elapsed time {:1.4f}ms".format((end-start)*10**(-6)))
start = time.thread_time_ns()
fil = cv.filter2D(img, -1,(3,3))
end = time.thread_time_ns()
print("Filter2D elapsed time {:1.4f}ms".format((end-start)*10**(-6)))

if __name__ == '__main__':
    while True:
        cv.imshow('After 3', img)
        cv.imshow('Own filter', new_img)
        cv.imshow('Filter2D', fil)
        cv.imshow('Blur', blur)
        key = cv.waitKey(10)
        if key == 27:
            cv.destroyAllWindows()
