import numpy as np
import cv2

I = cv2.imread('isfahan.jpg')
I = I.astype(np.float) / 255

sigma = 0.04  # initial standard deviation of noise

while True:

    N = np.random.rand(*I.shape) * sigma
    J = I + N

    cv2.imshow('snow noise', J)

    # press any key to exit
    key = cv2.waitKey(33)
    if key == ord('u'):  # if 'u' is pressed
        sigma += 0.02
    elif key == ord('d'):  # if 'd' is pressed
        sigma = sigma - 0.02 if sigma >= 0.02 else 0
    elif key == ord('q'):  # if 'q' is pressed then
        break  # quit

cv2.destroyAllWindows()
