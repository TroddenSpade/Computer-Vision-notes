import cv2
import numpy as np

I = cv2.imread('square.jpg')
G = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)

G = np.float32(G)
window_size = 2
soble_kernel_size  = 3 # kernel size for gradients
alpha = 0.04
H = cv2.cornerHarris(G,window_size,soble_kernel_size,alpha)

# normalize C so that the maximum value is 1
H = H / H.max()

# C[i,j] == 255 if H[i,j] > 0.01, and C[i,j] == 0 otherwise
C = np.uint8(H > 0.005) * 255

## connected components
# nc,CC = cv2.connectedComponents(C);

# to count the number of corners we count the number
# of nonzero elements of C (wrong way to count corners!)
n = np.count_nonzero(C) 

# Show corners as red pixels in the original image
I[C != 0] = [0,0,255]

cv2.imshow('corners',C)
cv2.waitKey(0) # press any key

font = cv2.FONT_HERSHEY_SIMPLEX 
cv2.putText(I,'There are %d corners!'%n,(20,40), font, 1,(0,0,255),2)
cv2.imshow('corners',I)
cv2.waitKey(0) # press any key

cv2.destroyAllWindows()

