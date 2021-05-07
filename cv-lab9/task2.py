import cv2
import numpy as np

NO_CORNERS = 78

def first_correct_scale(I):
    "find the smallest scale for which all corners are detected"

    psize = 6 # size of the pyramid
    
    # building the pyramid
    J = I.copy()
    Pyr = [J] # the first element is simply the original image
    for i in range(psize-1):
        J = cv2.pyrDown(J) # blurs, then downsamples by a factor of 2
        Pyr.append(J)

    for k in range(psize): # k = 0,1,..., psize-1
        J = Pyr[k]
        G = cv2.cvtColor(J,cv2.COLOR_BGR2GRAY)
        G = np.float32(G)
        
    
        win_size = 4 # do not change this!!
        soble_kernel_size  = 3 # kernel size for gradients
        alpha = 0.04

        H = cv2.cornerHarris(G,win_size,soble_kernel_size,alpha)
        H = H / H.max()
        
        C = np.uint8(H > 0.01) * 255
        nc,CC = cv2.connectedComponents(C);

        if nc-1 == NO_CORNERS: # if the connected components 
            return 2**k
        

I1 = cv2.imread('kntu1.jpg')
I2 = cv2.imread('kntu4.jpg')

sc1 = first_correct_scale(I1)
sc2 = first_correct_scale(I2)

J = np.concatenate((I1,I2), 1)

if sc1 < sc2:
    txt = 'Logo 1 is %d times smaller than logo 2'%(sc2/sc1)
elif sc1 > sc2:
    txt = 'Logo 1 is %d times larger than logo 2'%(sc1/sc2)
else:
    txt = 'Logo 1 is about the same size as logo 2'
    
cv2.putText(J,txt,(20,40), \
                cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)

cv2.imshow('scale',J)
cv2.waitKey(0)
