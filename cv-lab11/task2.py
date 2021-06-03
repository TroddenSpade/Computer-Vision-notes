import numpy as np
import cv2

I = cv2.imread('sign.jpg')

p1 = (135,105)
p2 = (331,143)
p3 = (356,292)
p4 = (136,290)

points1 = np.array([p1,p2,p3,p4], dtype=np.float32)

n = 480
m = 320
output_size = (n,m)

J = np.zeros((m,n)) # delete this!!

# mark corners of the plate in image I
for i in range(4):
    cv2.circle(I, (points1[i,0], points1[i,1]), 5, [0,0,255],2)

cv2.imshow('I', I);
cv2.waitKey(0)

cv2.imshow('J', J);
cv2.waitKey(0)
