import cv2 as cv

path = "../images/"


# saturacja czyli, przekroczenie zakresu przyjmuje górny lub dolny limit wartosci
# dst = alfa * img1 + beta * img2 + gamma

def alfa_callback(value):
    pass

def beta_callback(value):
    pass

def main():
    img1 = cv.imread(path + 'lenna_color.png')
    img2 = cv.imread(path + 'PUTVISION_LOGO.png')
    img1 = cv.resize(img1, dsize=img2.shape[0:2])
    alfaBlend = 0.3
    betaBlend = 0.7
    cv.namedWindow('blend')
    cv.createTrackbar('alpha', 'blend', 0, 100, alfa_callback)
    cv.createTrackbar('beta', 'blend', 0, 100, beta_callback)
    while True:
        dst = cv.addWeighted(img1, alfaBlend, img2, betaBlend, 0)
        cv.imshow('blend', dst)
        key = cv.waitKey(10)
        if key == 27:
            cv.destroyAllWindows()

        alfaBlend = cv.getTrackbarPos('alpha', 'blend') / 100.0

        betaBlend = cv.getTrackbarPos('beta', 'blend') / 100.0


        print("Alfa:= {a}, Beta:= {b}".format(a = alfaBlend, b = betaBlend))
            




def show(img):
    cv.imshow('show', img)
    cv.waitKey(500)
    cv.destroyAllWindows()
    

if __name__ == '__main__':
    main()
