import numpy as np
import cv2

I1 = cv2.imread('book2.jpg')
G1 = cv2.cvtColor(I1,cv2.COLOR_BGR2GRAY)

I2 = cv2.imread('scene.jpg')
G2 = cv2.cvtColor(I2,cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create() # opencv 3
# use "sift = cv2.SIFT()" if the above fails

keypoints1 = sift.detect(G1,None)
keypoints2 = sift.detect(G2,None)

cv2.drawKeypoints(G1,keypoints1,I1, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.drawKeypoints(G2,keypoints2,I2, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

print("No. of keypoints1 =", len(keypoints1))
print("No. of keypoints2 =", len(keypoints2))

# compute disriptor vectors
keypoints1, desc1 = sift.compute(G1, keypoints1); # opencv 3
keypoints2, desc2 = sift.compute(G2, keypoints2); # opencv 3


print("Descriptors1.shape =", desc1.shape)
print("Descriptors2.shape =", desc2.shape)

# pause here!!
input("Press ENTER to continue...")

# brute-force matching
bf = cv2.BFMatcher(crossCheck=False)

# for each descriptor in desc1 find its
# two nearest neighbours in desc2
matches = bf.knnMatch(desc1,desc2, k=2)
    
good_matches = []
alpha = 0.75
for m1,m2 in matches:
    # m1 is the best match
    # m2 is the second best match
    if m1.distance < alpha *m2.distance:
        good_matches.append(m1)

I = cv2.drawMatches(I1,keypoints1,I2,keypoints2, good_matches, None)

cv2.imshow('sift_keypoints1',I)
cv2.waitKey()
