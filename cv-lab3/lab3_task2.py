import cv2
import numpy as np
from matplotlib import pyplot as plt

fname = 'crayfish.jpg'
#fname = 'office.jpg'

I = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)

f, axes = plt.subplots(2, 3)

axes[0,0].imshow(I, 'gray', vmin=0, vmax=255)
axes[0,0].axis('off')

axes[1,0].hist(I.ravel(),256,[0,256]);

plt.show()


