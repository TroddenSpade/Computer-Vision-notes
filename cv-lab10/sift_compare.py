import numpy as np
import cv2

I1 = cv2.imread('book1.jpg')
G1 = cv2.cvtColor(I1,cv2.COLOR_BGR2GRAY)

I2 = cv2.imread('book2.jpg')
G2 = cv2.cvtColor(I2,cv2.COLOR_BGR2GRAY)

#sift = cv2.FeatureDetector_create("SIFT") # opencv 2.x.x
sift = cv2.xfeatures2d.SIFT_create() # opencv 3.x.x
# use "sift = cv2.SIFT()" if the above fails

keypoints1 = sift.detect(G1,None)
keypoints2 = sift.detect(G2,None)


cv2.drawKeypoints(G1,keypoints1,I1, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.drawKeypoints(G2,keypoints2,I2, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# concatenate the two images
I = np.concatenate((I1,I2), axis=1)

cv2.imshow('sift_keypoints1',I)
cv2.waitKey()
