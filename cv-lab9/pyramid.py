import numpy as np
import cv2
from matplotlib import pyplot as plt

I = cv2.imread('karimi.jpg')

psize = 6 # size of the pyramid (no. of levels)

# building the pyramid
J = I.copy()
Pyr = [J] # the first element is simply the original image
for i in range(psize-1):
    J = cv2.pyrDown(J) # blurs, then downsamples by a factor of 2
    Pyr.append(J)

# display the pyramid
# do not bother about the next two lines
size_list = [2**(psize-i-1) for i in range(psize)] 
f, ax = plt.subplots(1,psize, gridspec_kw={'width_ratios': size_list})

# do not change this (turns off the axes)
for a in ax.ravel():
    a.axis('off')

for l in range(psize):
    ax[l].set_title('l=%d'%l)
    J = Pyr[l]
    ax[l].imshow(J[:,:,::-1], interpolation='none');

plt.show()
