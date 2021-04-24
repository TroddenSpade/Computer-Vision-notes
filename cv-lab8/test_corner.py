import cv2
import numpy as np
import glob

fnames = glob.glob('*.jpg')

for filename in fnames:
    
    I = cv2.imread(filename)
    G = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
    G = np.float32(G)

    window_size = 3
    soble_kernel_size  = 3 # kernel size for gradients
    alpha = 0.04
    H = cv2.cornerHarris(G,window_size,soble_kernel_size,alpha)
    H = H / H.max()

    C = np.uint8(H > 0.01) * 255
    J = I.copy()
    J[C != 0] = [0,0,255]
    cv2.imshow('corners',J)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break


    # plot centroids of connected components as corner locations
    nC, CC, stats, centroids = cv2.connectedComponentsWithStats(C)

    J = I.copy()
    for i in range(1,nC):
        cv2.circle(J, (int(centroids[i,0]), int(centroids[i,1])), 3, (0,0,255))
    cv2.imshow('corners',J)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

        

    # fine-tune corner locations
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
    corners = cv2.cornerSubPix(G,np.float32(centroids),(5,5),(-1,-1),criteria)
    J = I.copy()
    for i in range(1,nC):
        cv2.circle(J, (int(corners[i,0]), int(corners[i,1])), 3, (0,0,255))
    cv2.imshow('corners',J)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

    
    

    
    
    

