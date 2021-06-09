import cv2
import numpy as np

def drawMatches(I1,keypoints1,I2,keypoints2, matches, I3=None):
    m1,n1,d1 = I1.shape
    m2,n2,d2 = I2.shape

    print(m1,n1,d1)
    print(m2,n2,d2)

    m = max(m1,m2)
    n = n1+n2

    I = np.zeros((m,n,d1), dtype = I1.dtype)

    print(I.shape)
    
    I[:m1,:n1,:] = I1
    I[:m2,n1:n,:] = I2
    
    for m in matches:
        i = m.queryIdx
        j = m.trainIdx

        x1 = int(keypoints1[i].pt[0])
        y1 = int(keypoints1[i].pt[1])

        x2 = int(keypoints2[j].pt[0]) + n1
        y2 = int(keypoints2[j].pt[1])

        b = np.random.randint(255)
        r = np.random.randint(255)
        g = np.random.randint(255)
        
        rad = 4
        cv2.circle(I, (x1,y1), rad, (b,r,g))
        cv2.circle(I, (x2,y2), rad, (b,r,g))
        cv2.line(I, (x1,y1), (x2,y2), (b,r,g))

    
    return I

 


if cv2.__version__[:cv2.__version__.find('.')] == '3':
    cv2.drawMatches = drawMatches
