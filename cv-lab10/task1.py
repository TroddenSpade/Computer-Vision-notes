import numpy as np
import cv2
import glob

sift = cv2.xfeatures2d.SIFT_create() # opencv 3
# use "sift = cv2.SIFT()" if the above fails

I2 = cv2.imread('scene.jpg')
G2 = cv2.cvtColor(I2,cv2.COLOR_BGR2GRAY)
keypoints2, desc2 = sift.detectAndCompute(G2, None); 

fnames = glob.glob('obj?.jpg')
fnames.sort()
for fname in fnames:

    I1 = cv2.imread(fname)
    G1 = cv2.cvtColor(I1,cv2.COLOR_BGR2GRAY)
    keypoints1, desc1 = sift.detectAndCompute(G1, None); 
    cv2.drawKeypoints(G1,keypoints2,I1)
    
    good_matches = []
            
    I = cv2.drawMatches(I1,keypoints1,I2,keypoints2,good_matches, None)
    
    no_matches = len(good_matches)
    if no_matches > 30:
        txt = "Object found! (matches = %d)"%no_matches
    else:
        txt = "Object not found! (matches = %d)"%no_matches

    cv2.putText(I,txt,(20,40),cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0),3)

    cv2.imshow('keypoints',I)

    if cv2.waitKey() & 0xFF == ord('q'):
        break

    
