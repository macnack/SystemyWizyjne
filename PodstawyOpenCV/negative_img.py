import cv2
import numpy as np

lenna = cv2.imread("../images/lenna_color.png", cv2.IMREAD_COLOR )
img = np.ones(lenna.shape, dtype=np.uint8)


def negative(img):
    neg = np.ones(img.shape, dtype=np.uint8)
    neg *= 255
    return neg - img

if __name__ == '__main__':
    cv2.imshow("Negative", negative(lenna))
    cv2.waitKey(2000)
    cv2.destroyAllWindows()
