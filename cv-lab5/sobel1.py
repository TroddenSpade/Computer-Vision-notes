import numpy as np
import cv2
from matplotlib import pyplot as plt

I = cv2.imread("agha-bozorg.jpg", cv2.IMREAD_GRAYSCALE)

# Compute the gradient in x direction using the sobel filter

# Method 1: using filter2D **********

Dx = np.array([[-1, 0, 1],
               [-2, 0, 2],
               [-1, 0, 1]]); # Sobel filter

Ix = cv2.filter2D(I, -1, Dx); 
print(I.dtype)
print(Ix.dtype)

Ix = cv2.filter2D(I, cv2.CV_16S, Dx); # cv2.CV_16S: 16 bit signed integer
print(Ix.dtype)

input('press ENTER to continue... ')

# Method 2: using sobel function **********
Ix2 = cv2.Sobel(I,cv2.CV_16S,1,0)

print(np.abs(Ix - Ix2).max())

input('press ENTER to continue... ')

# Plot the gradient image
f, axes = plt.subplots(2, 2)

axes[0,0].imshow(I,cmap = 'gray')
axes[0,0].set_title("Original Image")

axes[0,1].imshow(Ix,cmap = 'gray')
axes[0,1].set_title("Ix (cv2.filter2D)")

axes[1,0].imshow(Ix2,cmap = 'gray')
axes[1,0].set_title("Ix2 (cv2.Sobel)")

axes[1,1].imshow(np.abs(Ix),cmap = 'gray')
axes[1,1].set_title("abs(Ix)")

# Notice that imshow in matplotlib considers the minimums value of I
# as black and the maximum value as white (this is different from
# the behaviour in cv2.imshow
plt.show()

