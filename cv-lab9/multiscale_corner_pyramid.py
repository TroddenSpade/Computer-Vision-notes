import cv2
import numpy as np

I = cv2.imread('kntu1.jpg')

psize = 6 # size of the pyramid (no. of levels)

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
    
    win_size = 4 # do not change this
    soble_kernel_size  = 3 # kernel size for gradients
    alpha = 0.04
    H = cv2.cornerHarris(G,win_size,soble_kernel_size,alpha)
    H = H / H.max()
    
    C = np.uint8(H > 0.01) * 255
    nc,CC = cv2.connectedComponents(C);
    
    J[C != 0] = [0,0,255]
    
    JJ = np.zeros(I.shape,dtype=I.dtype)
    JJ[:J.shape[0],:J.shape[1],:] = J;
    cv2.putText(JJ,'scale=1/%d, corners=%d'%(2**k, nc-1),(360,30), \
                cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)
    
    cv2.imshow('corners',JJ)
    
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
    
