import cv2
import numpy as np

I = cv2.imread('damavand.jpg')
J = cv2.imread('eram.jpg')

print(I.shape)
print(J.shape)

K = I.copy()
cv2.imshow('transition', K)
cv2.waitKey()

for i in range(101):
    beta = i * 0.01
    alpha = 1 - beta
    gamma = 0
    K = cv2.addWeighted(I, alpha, J, beta, gamma)
    cv2.imshow('transition', K)
    cv2.waitKey(20)

cv2.waitKey()
cv2.destroyAllWindows()
