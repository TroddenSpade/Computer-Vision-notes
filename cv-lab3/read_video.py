import numpy as np
import cv2

# create a VideoCapture object
cap = cv2.VideoCapture('kntu-computer.avi')

# sometimes this is needed:
#if not cap.isOpened():
#    cap.open();


while True:
    
    # Capture frame-by-frame
    ret, I = cap.read()
    
    if ret == False: # end of video (perhaps)
        break

    # Display I
    cv2.imshow('win1',I)
    
    key = cv2.waitKey(33) # ~ 30 frames per second

    if key & 0xFF == ord('q'): 
        break


cap.release()
cv2.destroyAllWindows()


