import cv2 as cv


def after_three_is_white(img):
    for idx_col in range(img.shape[1]):
        if not(idx_col % 3):
            img[:, idx_col] = 255
    return img

def filterKuwahara(img, kernel_size):
    sub_kernel_size = int(kernel_size/2)
    border_img = cv.copyMakeBorder(img, kernel_size, kernel_size, kernel_size, kernel_size, cv.BORDER_CONSTANT)
    output = img.copy()
    for row in range(img.shape[0]):

        for col in range(img.shape[1]):
            sub_kernels = []
            kernel = border_img[row: row + kernel_size, col: col + kernel_size]
            sub_kernels.append(kernel[0:sub_kernel_size+1, :sub_kernel_size+1])
            sub_kernels.append(kernel[sub_kernel_size:, :sub_kernel_size+1])
            sub_kernels.append(kernel[0:sub_kernel_size+1, sub_kernel_size:])
            sub_kernels.append(kernel[sub_kernel_size:, sub_kernel_size:])

            mean_std = [cv.meanStdDev(r) for r in sub_kernels]
            output[row, col] = min(mean_std, key=lambda x: x[1])[0]

    return output

if __name__ == '__main__':
    img = cv.imread("../images/lenna_color.png", cv.IMREAD_GRAYSCALE)
    img = after_three_is_white(img=img)
    imgKuwahara = filterKuwahara(img, 5)
    while True:
        cv.imshow('Kuwahara filter', imgKuwahara)
        cv.imshow('Image', img)
        key = cv.waitKey(10)
        if key == 27:
            cv.destroyAllWindows()
