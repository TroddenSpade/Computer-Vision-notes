import numpy as np
import cv2

I = cv2.imread('isfahan.jpg', cv2.IMREAD_GRAYSCALE);
I = I.astype(np.float) / 255

sigma = 0.04 # initial standard deviation of noise 

while True:
    
    J = I; # change this line so J is the noisy image
    
    cv2.imshow('snow noise',J)
    
    # press any key to exit
    key = cv2.waitKey(33)
    if key & 0xFF == ord('u'): # if 'u' is pressed 
        pass # increase noise
    elif key & 0xFF == ord('d'):  # if 'd' is pressed 
        pass # decrease noise 
    elif key & 0xFF == ord('q'):  # if 'q' is pressed then 
        break # quit
    
cv2.destroyAllWindows()
