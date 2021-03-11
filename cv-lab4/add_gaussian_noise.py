# Introduction to Computer Vision (Undergrad)
# School of Computer Engineering
# K.N. Toosi University of Technology

import numpy as np
import cv2

I = cv2.imread('isfahan.jpg');

# convert I to floating point from unsigned integer
# Note: For displaying floating point images the maximum
# intensity has to be 1 instead of 255
I = I.astype(np.float) / 255

# create the noise image
sigma = 0.04 # notice maximum intensity is 1
N = np.random.randn(*I.shape) * sigma

# add noise to the original image
J = I+N; # or use cv2.add(I,N);

cv2.imshow('original',I)
cv2.waitKey(0) # press any key to exit

cv2.imshow('noisy image',J)
cv2.waitKey(0) # press any key to exit

cv2.destroyAllWindows()

