import numpy as np
import cv2
from matplotlib import pyplot as plt

I = cv2.imread('karimi.jpg')
s = 4; # downsize with a factor of s

# Downsize by sampling every s pixels:
J = I[::s, ::s, :]

Jb = Jg = J

# blur with a box filter, then downsample
ksize = s + 1;
Ib = cv2.boxFilter(I, -1, (ksize,ksize))
Jb = Ib[::s, ::s, :]


# blur with a Gaussian filter, then resample
sigma = (s+1)/np.sqrt(12) # equivant sigma for Guassian kernel
Ig = cv2.GaussianBlur(I, (0,0),sigma)
Jg = Ig[::s, ::s, :]

f, ax = plt.subplots(2,3, gridspec_kw={'height_ratios': [s,1]})

# do not change this (turns off the axes)
for a in ax.ravel():
    a.axis('off')

ax[0,1].set_title('Original')
ax[0,1].imshow(I[:,:,::-1])

ax[1,0].set_title('Downsized')
ax[1,0].imshow(J[:,:,::-1], interpolation='none')

ax[1,1].set_title('Box Blur + Downsized')
ax[1,1].imshow(Jb[:,:,::-1], interpolation='none')

ax[1,2].set_title('Gaussian Blur + Downsized')
ax[1,2].imshow(Jg[:,:,::-1], interpolation='none')

plt.show()
