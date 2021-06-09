import numpy as np
import cv2
import glob

sift = cv2.xfeatures2d.SIFT_create() # opencv 3
# use "sift = cv2.SIFT()" if the above fails

I2 = cv2.imread('scene.jpg')
G2 = cv2.cvtColor(I2,cv2.COLOR_BGR2GRAY)
keypoints2, desc2 = sift.detectAndCompute(G2, None); # opencv 3

fnames = glob.glob('obj?.jpg')
fnames.sort()
for fname in fnames:

    I1 = cv2.imread(fname)
    G1 = cv2.cvtColor(I1,cv2.COLOR_BGR2GRAY)
    keypoints1, desc1 = sift.detectAndCompute(G1, None); # opencv 3

    
    H = np.eye(3,dtype=np.float32) # this needs to be changed!!

    J = cv2.warpPerspective(I1, H, (I2.shape[1],I2.shape[0]) )

    # alternatingly show images I2 and J
    ind = 0;
    imgs = [I2, J]
    while 1:
        ind = 1-ind

        cv2.imshow('Reg',imgs[ind])
        key =  cv2.waitKey(800) 
                
        if key & 0xFF == ord('q'):
            exit()
        elif key & 0xFF != 0xFF:
            break


        

    
