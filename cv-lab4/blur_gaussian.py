import numpy as np
import cv2

I = cv2.imread('isfahan.jpg').astype(np.float64) / 255;

m = 13; # we will create an m by m filter

# create a 1D Gaussian filter
Fg = cv2.getGaussianKernel(m, sigma=-1);
# by setting sigma=-1, the value of sigma is computed 
# automatically as: sigma = 0.3*((ksize-1)*0.5 - 1) + 0.8

print(Fg)
print(Fg.shape) # Fg is 1-dimensional (m by 1)

exit() # delete this to continue

# Now we create a 2D filter
# We use matrix multiplication to create an m by m 2D filter
# out of "m by 1" and "1 by m" 1D filters, which in this case happens
# to be the same thing as correlation between 1D filters
Fg =  Fg.dot(Fg.T) # an "m by 1" matrix multiplied by a "1 by m" matrix

print(Fg)
print(Fg.shape)

exit() # delete this to continue

# filter the image with the Gaussian filter
Jg = cv2.filter2D(I,-1, Fg)

cv2.imshow('original',I)
cv2.waitKey()

cv2.imshow('blurred_Gaussian',Jg)
cv2.waitKey()

cv2.destroyAllWindows()
