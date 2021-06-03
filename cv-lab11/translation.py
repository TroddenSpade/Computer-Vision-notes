import cv2
import numpy as np

I = cv2.imread('karimi.jpg')

# translations in x and y directions
tx = 100
ty = 40

# use an affine transformation matrix (2x3)
M = np.array([[1, 0, tx],
              [0, 1, ty]]).astype(np.float32)

output_size = (I.shape[1],I.shape[0]) # output image size
#output_size = (I.shape[1]+200, I.shape[0]+200);

J = cv2.warpAffine(I,M,output_size)

cv2.imshow('I',I)
cv2.waitKey(0)

cv2.imshow('J',J)
cv2.waitKey(0)

#! use a homography transformation matrix (3x3)
#H = np.array([[1, 0, tx],
#              [0, 1, ty],
#              [0, 0, 1]]).astype(np.float32)
#K = cv2.warpPerspective(I,H, output_size)
#cv2.imshow('K',K)
#cv2.waitKey(0)

cv2.destroyAllWindows()




