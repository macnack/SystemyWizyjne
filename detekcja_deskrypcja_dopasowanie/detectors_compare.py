from os import listdir
from os.path import isfile, join
import time
import cv2 as cv
import numpy as np

images_dir = "./images/"
images = [join(images_dir, f) for f in listdir(images_dir) if isfile(join(images_dir, f))]
images = sorted(images)
#Porównać czas wykonywania i dokładność
for img_path in images[:3]:
    img = cv.imread(img_path)
    img_fast = img.copy()
    img_sift = img.copy()
    img_orb = img.copy()
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    #FAST
    start = time.thread_time_ns()
    fast_detector = cv.FastFeatureDetector_create()
    fast_kp = fast_detector.detect(gray, None)
    end = time.thread_time_ns()
    fast_calc = "FAST kp time:= {:1.4f}ms".format((end-start)*10**(-6))
    brief = cv.xfeatures2d.BriefDescriptorExtractor_create()
    kp_fast, des_dast = brief.compute(gray, fast_kp)
    #SIFT
    start = time.thread_time_ns()
    sift_detector = cv.SIFT_create()
    sift_kp = sift_detector.detect(gray, None)
    end = time.thread_time_ns()
    sift_calc = "SIFT kp time:= {:1.4f}ms".format((end-start)*10**(-6))
    kp_sift, des_sift = sift_detector.compute(gray, sift_kp)

    #ORB
    start = time.thread_time_ns()
    orb_descriptor = cv.ORB_create()
    orb_kp = orb_descriptor.detect(gray, None)
    end = time.thread_time_ns()
    orb_calc = "ORB kp time:= {:1.4f}ms".format((end-start)*10**(-6))
    kp_orb, des_orb = orb_descriptor.compute(gray, orb_kp)



    print()
    print(img_path)
    print(fast_calc, ', ', sift_calc, ', ', orb_calc, ' ')
    print("Fast size:={}, ".format(len(fast_kp)), "SIFT size:={}, ".format(len(sift_kp)), "ORB size:={}".format(len(orb_kp)), )
    cv.drawKeypoints(gray,fast_kp,img_fast)
    cv.drawKeypoints(gray,sift_kp,img_sift)
    cv.drawKeypoints(gray, orb_kp, img_orb)
    img_output = np.concatenate((img, img_fast, img_sift, img_orb), axis=1)
    cv.imshow("Img: {}".format(img_path), img_output)
    cv.waitKey(300)

