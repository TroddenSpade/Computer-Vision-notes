import cv2
import numpy as np
from matplotlib import pyplot as plt

I = cv2.imread('masoleh.jpg')
# notice that OpenCV uses BGR instead of RGB!
B = I.copy()
B[:, :, 1:] = 0

G = I.copy()
G[:, :, ::2] = 0

R = I.copy()
R[:, :, :2] = 0


cv2.imshow('win1', I)

while 1:
    k = cv2.waitKey()

    if k == ord('o'):
        cv2.imshow('win1', I)
    elif k == ord('b'):
        cv2.imshow('win1', B)
    elif k == ord('g'):
        cv2.imshow('win1', G)
    elif k == ord('r'):
        cv2.imshow('win1', R)
    elif k == ord('q'):
        cv2.destroyAllWindows()
        break
