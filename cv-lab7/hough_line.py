import numpy as np
import cv2


def draw_line(Img, rho, theta):
    """draws a line in an image 'Img' given 'rho' and 'theta'"""
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * a)
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * a)

    cv2.line(Img, (x1, y1), (x2, y2), (0, 0, 255), 1)


Img = cv2.imread('highway.jpg')

G = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)  # -> grayscale

E = cv2.Canny(G, 100, 200)  # find the edges

min_votes = 160  # minimum votes to be considered a line
distance_resolution = 1  # 1 pixel: resolution of the parameter "rho" (distance to origin)
angle_resolution = np.pi / 180  # pi/180 radians: resolution (bin size) of the parameter "theta"
L = cv2.HoughLines(E, distance_resolution, angle_resolution, min_votes)

# draw the lines
for [[rho, theta]] in L:
    draw_line(Img, rho, theta)

cv2.imshow("E", E)
cv2.imshow("Img", Img)
cv2.waitKey(0)
cv2.destroyAllWindows()
