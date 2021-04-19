import numpy as np
import cv2

Img = cv2.imread('coins.jpg')
G = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)
G = cv2.GaussianBlur(G, (5, 5), 0)

canny_high_threshold = 160
min_votes = 30  # minimum no. of votes to be considered as a circle
min_centre_distance = 40

resolution = 1  # resolution of parameters (centre, radius) relative to image resolution
circles = cv2.HoughCircles(G, cv2.HOUGH_GRADIENT, resolution, min_centre_distance,
                           param1=canny_high_threshold,
                           param2=min_votes, minRadius=0, maxRadius=100)

for c in circles[0, :]:
    x = int(c[0])  # x coordinate of the centre
    y = int(c[1])  # y coordinate of the centre
    r = int(c[2])  # radius
    cv2.circle(Img, (x, y), r, (0, 255, 0), 2)

print(circles)

n = len(circles[0, :])
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(Img, f'There are {n} coins!', (400, 40), font, 1, (255, 0, 0), 2)

cv2.imshow("Img", Img)
cv2.waitKey(0)
