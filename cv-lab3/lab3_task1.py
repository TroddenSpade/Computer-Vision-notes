import numpy as np
import cv2

# create a VideoCapture object
cap = cv2.VideoCapture('eggs.avi')

# get the dimensions of the frame
# you can also read the first frame to get these
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # width of the frame
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # height of the frame

fourcc = cv2.VideoWriter_fourcc(*'XVID') # choose codec

# opencv 2.x:
#w = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)) 
#h = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)) 
#fourcc = cv2.cv.CV_FOURCC(*'XVID')

# create VideoWriter object w by h, 30 frames per second
out = cv2.VideoWriter('eggs-reverse.avi',fourcc, 30.0, (w,h))

while True:
    ret, I = cap.read()

    if ret == False: # end of video (or error)
        break

    # write the current frame I
    out.write(I)

cap.release()
out.release()
