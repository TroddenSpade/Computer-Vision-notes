import numpy as np
import cv2
from matplotlib import pyplot as plt

I = cv2.imread("agha-bozorg.jpg", cv2.IMREAD_GRAYSCALE)

# Sobel gradient in the x direction
Ix = cv2.Sobel(I,cv2.CV_64F,1,0)
print(Ix.dtype)

# Sobel gradient in the y direction
Iy = cv2.Sobel(I,cv2.CV_64F,0,1)
print(Iy.dtype)

# Magnitude of gradient
E = np.sqrt(Ix*Ix + Iy*Iy) 

# Plot the gradient image
f, axes = plt.subplots(2, 2)

axes[0,0].imshow(I,cmap = 'gray')
axes[0,0].set_title("Original Image")

axes[0,1].imshow(abs(Ix),cmap = 'gray')
axes[0,1].set_title("abs(Ix)")


axes[1,0].imshow(abs(Iy),cmap = 'gray')
axes[1,0].set_title("abs(Iy)")

axes[1,1].imshow(E,cmap = 'gray')
axes[1,1].set_title("Magnitude of Gradient")

# Notice that imshow in matplotlib considers the minimums value of I
# as black and the maximum value as white (this is different from
# the behaviour in cv2.imshow
plt.show()
