import numpy as np
import cv2
from matplotlib import pyplot as plt

def std_filter(I, ksize):
    F = np.ones((ksize,ksize), dtype=np.float) / (ksize*ksize);
       
    MI = cv2.filter2D(I,-1,F) # apply mean filter on I

    I2 = I * I; # I squared
    MI2 = cv2.filter2D(I2,-1,F) # apply mean filter on I2

    return np.sqrt(MI2 - MI * MI)

def zero_crossing(I):
    """Finds locations at which zero-crossing occurs, used for
    Laplacian edge detector"""
    
    Ishrx = I.copy();
    Ishrx[:,1:] = Ishrx[:,:-1]
        
    Ishdy = I.copy();
    Ishdy[1:,:] = Ishdy[:-1,:]
        
    ZC = (I==0) | (I * Ishrx < 0) | (I * Ishdy < 0); # zero crossing locations

    SI = std_filter(I, 3) / I.max()

    Mask =  ZC & (SI > .1)

    E = Mask.astype(np.uint8) * 255 # the edges

    return E
    
I = cv2.imread("agha-bozorg.jpg", cv2.IMREAD_GRAYSCALE)

# set the sigma for Gaussian Blurring
sigma = 7

# Sobel magnitude of gradient 
thresh = 90 # threshold
Ib = cv2.GaussianBlur(I, (sigma,sigma), 0); # blur the image
Ix = cv2.Sobel(Ib,cv2.CV_64F,1,0)
Iy = cv2.Sobel(Ib,cv2.CV_64F,0,1)
Es = np.sqrt(Ix*Ix + Iy*Iy) 
Es = np.uint8(Es > thresh)*255 # threshold the gradients

# Laplacian of Gaussian
# Here, we first apply a Gaussian filter and then apply
# the Laplacian operator (instead of apply the LoG filter)
Ib = cv2.GaussianBlur(I, (sigma,sigma), 0);
El = cv2.Laplacian(Ib,cv2.CV_64F,ksize=5)
El = zero_crossing(El);

# Canny Edge detector
lth = 50   # low threshold
hth = 120  # high threshold
Ib = cv2.GaussianBlur(I, (sigma,sigma), 0); # blur the image
Ec = cv2.Canny(Ib,lth, hth)

f, axes = plt.subplots(2, 2)

axes[0,0].imshow(I,cmap = 'gray')
axes[0,0].set_title("Original Image")

axes[0,1].imshow(Es,cmap = 'gray')
axes[0,1].set_title("Sobel")


axes[1,0].imshow(El,cmap = 'gray')
axes[1,0].set_title("Laplacian")

axes[1,1].imshow(Ec,cmap = 'gray')
axes[1,1].set_title("Canny")

# Notice that imshow in matplotlib considers the minimums value of I
# as black and the maximum value as white (this is different from
# the behaviour in cv2.imshow)
plt.show()
