import numpy as np
import cv2
import glob

for fname in glob.glob('*.jpg'):

    I = cv2.imread(fname)
    G = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)

    #sift = cv2.FeatureDetector_create("SIFT") # opencv 2.x.x
    sift = cv2.xfeatures2d.SIFT_create() # opencv 3.x.x
    # use "sift = cv2.SIFT()" if the above fails
    
    keypoints = sift.detect(G,None)

    cv2.drawKeypoints(G,keypoints,I)
    #cv2.drawKeypoints(G,keypoints,I, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


    # display keypoint properties
    # for kp in keypoints:
    #    print('-'*40)
    #    print('location=(%.2f,%.2f)'%(kp.pt[0], kp.pt[1]))
    #    print('orientation angle=%1.1f'%kp.angle)
    #    print('scale=%f'%kp.size)
    
    
    cv2.putText(I,"Press 'q' to quit, any key for next image",(20,20), \
                cv2.FONT_HERSHEY_SIMPLEX, .5,(255,0,0),1)

    cv2.imshow('sift_keypoints',I)

    if cv2.waitKey() & 0xFF == ord('q'):
        break

