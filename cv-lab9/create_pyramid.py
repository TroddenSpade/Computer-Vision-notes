import numpy as np
import cv2

I = cv2.imread('karimi.jpg')
m,n,_ = I.shape

P1 = np.array([[0,0], [0, m-1], [n-1,0], [n-1,m-1]])

psize = 7 # size of the pyramid (no. of levels)

# building the pyramid

J = np.ones((600,500,3), dtype=np.uint8)*255
m2,n2,_ = J.shape

v  = np.array([(n2//2,0)])
P2 = np.array([(0,4*m2//5),
               (5*n2//6,m2),
               (3*n2//12,7*m2//12),
               (n2,8*m2//12)])

cv2.line(I, (0,0), (0,m-1), (1,1,1),4)
cv2.line(I, (0,0), (n-1,0), (1,1,1),4)
cv2.line(I, (n-1,m-1), (0,m-1), (1,1,1),4)
cv2.line(I, (n-1,m-1), (n-1,0), (1,1,1),4)

for i in range(4):
    cv2.line(J, (v[0,0],v[0,1]), (P2[i,0],P2[i,1]), (0,0,0),2)

p21 = P2[1].copy()
    
for i in range(psize):
    H, status = cv2.findHomography(P1, P2)

    K = cv2.warpPerspective(I, H, (J.shape[1],J.shape[0]))

    msk = K.max(axis=2) != 0

    J[msk,:] = K[msk,:]

    cv2.line(J, (v[0,0],v[0,1]), (p21[0],p21[1]), (0,0,0),2)

    cv2.imshow('',J)
    cv2.waitKey()
    
    P2 = (P2 + v)/2



