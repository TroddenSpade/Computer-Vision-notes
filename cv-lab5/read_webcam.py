import numpy as np
import cv2

cam_id = 0  # camera id

# for default webcam, cam_id is usually 0
# try out other numbers (1,2,..) if this does not work

cap = cv2.VideoCapture(cam_id)


while True:
    ret, I = cap.read();


    cv2.imshow("my stream", I);


    # press "q" to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()







