import cv2
import numpy as np

NO_CORNERS = 78

def first_correct_winsize(I):
    "find the smallest win_size for which all corners are detected"
    G = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
    G = np.float32(G)
    for k in range(1,7):
        win_size = 2**k # 2^k
        soble_kernel_size  = 3
        alpha = 0.04
        H = cv2.cornerHarris(G,win_size,soble_kernel_size,alpha)
        H = H / H.max()
        
        C = np.uint8(H > 0.01) * 255
        nc,CC = cv2.connectedComponents(C);

        if nc-1 == 78:
            return win_size
    
    return 0 # incorrect


I1 = cv2.imread('kntu1.jpg')
I2 = cv2.imread('kntu4.jpg')

s1 = first_correct_winsize(I1)
s2 = first_correct_winsize(I2)
    
J = np.concatenate((I1,I2), 1)

if s1 < s2:
    txt = 'Logo 1 is %d times smaller than logo 2'%(s2/s1)
elif s1 > s2:
    txt = 'Logo 1 is %d times larger than logo 2'%(s1/s2)
else:
    txt = 'Logo 1 is about the same size as logo 2'
    
cv2.putText(J,txt,(20,40), \
                cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)

cv2.imshow('scale',J)
cv2.waitKey(0)
    
    
