import cv2
import numpy as np
import time

cube = "../images/qr.jpg"

img = cv2.imread(cube, cv2.IMREAD_COLOR)

cv2.imshow("cube", img)
start = time.thread_time_ns()
imgInterLinear = cv2.resize(img, None, fx=1, fy = 2.75, interpolation=cv2.INTER_LINEAR)
end = time.thread_time_ns()
cv2.imshow("INTER_LINEAR, elapsed time:= {:1.4f}ms".format((end-start)*10**(-6)), imgInterLinear)

start = time.thread_time_ns()
imgInterLinear = cv2.resize(img, None, fx=1, fy = 2.75, interpolation=cv2.INTER_NEAREST)
end = time.thread_time_ns()
cv2.imshow("INTER_NEAREST, elapsed time:= {:1.4f}ms".format((end-start)*10**(-6)), imgInterLinear)

start = time.thread_time_ns()
imgInterLinear = cv2.resize(img, None, fx=1, fy = 2.75, interpolation=cv2.INTER_AREA)
end = time.thread_time_ns()
cv2.imshow("INTER_AREA, elapsed time:= {:1.4f}ms".format((end-start)*10**(-6)), imgInterLinear)

start = time.thread_time_ns()
imgInterLinear = cv2.resize(img, None, fx=1, fy = 2.75, interpolation=cv2.INTER_LANCZOS4)
end = time.thread_time_ns()
cv2.imshow("INTER_LANCZOS4, elapsed time:= {:1.4f}ms".format((end-start)*10**(-6)), imgInterLinear)
cv2.waitKey()
