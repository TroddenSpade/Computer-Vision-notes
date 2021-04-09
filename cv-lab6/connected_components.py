import numpy as np
import cv2

I = cv2.imread('img1.bmp', cv2.IMREAD_GRAYSCALE)

n,C = cv2.connectedComponents(I);

print("n=%d"%n)
print(np.unique(I))
print(np.unique(C))

cv2.imshow('I', I)
cv2.waitKey(0) # press any key to continue...

for k in range(n):

    # show the k-th connected component
    Ck = np.zeros(I.shape, dtype=I.dtype)
    Ck[C == k] = 255;

    cv2.imshow('C%d'%k, Ck)
    cv2.waitKey(0) # press any key to continue...


I = cv2.cvtColor(I,cv2.COLOR_GRAY2BGR)

font = cv2.FONT_HERSHEY_SIMPLEX 

# note: background is also counted as a connected component by openCV
cv2.putText(I,'There are %d connected components!'%(n-1),(20,40), font, 1,(0,0,255),2)

cv2.imshow('Num', I)
cv2.waitKey(0)

