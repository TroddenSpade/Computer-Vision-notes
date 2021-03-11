import numpy as np
import cv2

I = cv2.imread('branches2.jpg').astype(np.float64) / 255

noise_sigma = 0.04  # initial standard deviation of noise

m = 1  # initial filter size,

gm = 3  # gaussian filter size

size = 9  # bilateral filter size
sigmaColor = 0.3
sigmaSpace = 75

# with m = 1 the input image will not change
filter = 'b'  # box filter

while True:

    # add noise to image
    N = np.random.rand(*I.shape) * noise_sigma
    J = I + N

    if filter == 'b':
        # filter with a box filter
    elif filter == 'g':
        # filter with a Gaussian filter
        pass
    elif filter == 'l':
        # filter with a bilateral filter
        pass

    # filtered image

    cv2.imshow('img', K)
    key = cv2.waitKey(30) & 0xFF

    if key == ord('b'):
        filter = 'b'  # box filter
        print('Box filter')

    elif key == ord('g'):
        filter = 'g'  # filter with a Gaussian filter
        print('Gaussian filter')

    elif key == ord('l'):
        filter = 'l'  # filter with a bilateral filter
        print('Bilateral filter')

    elif key == ord('+'):
        # increase m
        m = m + 2
        print('m=', m)

    elif key == ord('-'):
        # decrease m
        if m >= 3:
            m = m - 2
        print('m=', m)
    elif key == ord('u'):
        # increase noise
        pass
    elif key == ord('d'):
        # decrease noise
        pass
    elif key == ord('p'):
        # increase gm
        pass
    elif key == ord('n'):
        # decrease gm
        pass
    elif key == ord('>'):
        # increase size
        pass
    elif key == ord('<'):
        # decrease size
        pass
    elif key == ord('q'):
        break  # quit

cv2.destroyAllWindows()
