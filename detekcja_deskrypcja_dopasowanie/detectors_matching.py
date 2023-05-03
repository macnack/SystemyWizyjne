from os import listdir
from os.path import isfile, join
import time
import cv2 as cv
import numpy as np


images_dir = "./images/"
images = [join(images_dir, f)
          for f in listdir(images_dir) if isfile(join(images_dir, f))]
images = sorted(images)
match_imgs = {}
match_imgs[images[5]] = images[0]
match_imgs[images[7]] = images[6]
match_imgs[images[9]] = images[6]
match_imgs[images[15]] = images[11]
# Porównać dopasowania i dokładność
def match_des(source, des1, kp1, target,des2, kp2, norm):
    # create matcher
    bf = cv.BFMatcher(norm, crossCheck=True)

    #match descriptors
    matches = bf.match(des1, des2)

    #Sort them in the order of their distance.
    matches = sorted(matches, key= lambda x:x.distance)
    return cv.drawMatches(source, kp1, target, kp2, matches[:20], None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

for target_path, source_path  in match_imgs.items():
    source = cv.imread(source_path)
    # source = cv.resize(source, None, fx=.8, fy =.8, interpolation=cv.INTER_LINEAR)
    source_gray = cv.cvtColor(source, cv.COLOR_BGR2GRAY)

    target = cv.imread(target_path)
    # target = cv.resize(target, None, fx=.8, fy =.8, interpolation=cv.INTER_LINEAR)
    target_gray = cv.cvtColor(target, cv.COLOR_BGR2GRAY)

    # FAST
    fast_detector = cv.FastFeatureDetector_create()
    fast_kp1 = fast_detector.detect(source_gray, None)
    fast_kp2 = fast_detector.detect(target_gray, None)

    brief = cv.xfeatures2d.BriefDescriptorExtractor.create()
    kp1_fast, des1_brief = brief.compute(source_gray, fast_kp1)
    kp2_fast, des2_brief = brief.compute(target_gray, fast_kp2)

    img_output_brief = match_des(source, des1_brief, kp1_fast, target, des2_brief, kp2_fast, cv.NORM_HAMMING)
    # SIFT
    sift_detector = cv.SIFT_create()
    kp1_sift, des1_sift = sift_detector.detectAndCompute(source_gray, None)
    kp2_sift, des2_sift = sift_detector.detectAndCompute(target_gray, None)

    img_output_sift = match_des(source, des1_sift, kp1_sift, target, des2_sift, kp2_sift, cv.NORM_L2)
    # ORB
    orb_descriptor = cv.ORB_create()
    kp1_orb, des1_orb = orb_descriptor.detectAndCompute(source_gray, None)
    kp2_orb, des2_orb = orb_descriptor.detectAndCompute(target_gray, None)

    img_output_orb = match_des(source, des1_orb, kp1_orb, target, des2_orb, kp2_orb, cv.NORM_HAMMING)
    
    img_output = np.concatenate( (img_output_brief, img_output_sift, img_output_orb), axis=0)
    window_name = "Matching {} with {}".format(target_path, source_path)
    cv.namedWindow(window_name)
    if True:
        cv.imshow(window_name, img_output)
        key_code = cv.waitKey(0)
    cv.destroyAllWindows()
    