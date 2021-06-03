import cv2
import numpy as np

I = cv2.imread('karimi.jpg')

tx = 100
ty = 60

th =  20 # angle of rotation (degrees)
th *= np.pi / 180 # convert to radians

s = 0.6 # scale factor

M = np.array([[s*np.cos(th),-s*np.sin(th),tx],
              [s*np.sin(th), s*np.cos(th),ty]])

output_size = (I.shape[1], I.shape[0])
J = cv2.warpAffine(I,M,  output_size)

cv2.imshow('I',I)
cv2.waitKey(0)

cv2.imshow('J',J)
cv2.waitKey(0)
