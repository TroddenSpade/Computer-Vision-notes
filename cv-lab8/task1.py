import cv2
import numpy as np

I = cv2.imread('polygons.jpg')
G = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)

ret, T = cv2.threshold(G,220,255,cv2.THRESH_BINARY_INV)

nc1,CC1 = cv2.connectedComponents(T)

for k in range(1,nc1):

    Ck = np.zeros(T.shape, dtype=np.float32)
    Ck[CC1 == k] = 1;
    Ck = cv2.GaussianBlur(Ck,(5,5),0)
    Ck = cv2.cvtColor(Ck,cv2.COLOR_GRAY2BGR)

    # Now, apply corner detection on Ck

    
    font = cv2.FONT_HERSHEY_SIMPLEX 
    cv2.putText(Ck,'There are %d vertices!'%(100),(20,30), font, 1,(0,0,255),1)

    
    cv2.imshow('corners',Ck)
    cv2.waitKey(0) # press any key



