import cv2
import numpy as np
from sklearn.linear_model import RANSACRegressor

img = cv2.imread('red.png')

#convert to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#grab red (specific boundries bc it's a pain)
lower_red = np.array([0, 70, 50])
upper_red = np.array([10, 255, 255])
mask1 = cv2.inRange(hsv, lower_red, upper_red)

lower_red = np.array([170, 70, 50])
upper_red = np.array([180, 255, 255])
mask2 = cv2.inRange(hsv, lower_red, upper_red)

mask = mask1 + mask2

#morphological operations
kernel = np.ones((5, 5), np.uint8)
mask = cv2.erode(mask, kernel, iterations=1)
mask = cv2.dilate(mask, kernel, iterations=1)

#find contours
contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# draw boxes around red objects and filter out very large and very small boxes 
boxes = []
for contour in contours:
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)
    if (500 < area < 4000) and (90 < perimeter < 300):
        rect = cv2.minAreaRect(contour)
        box = cv2.boxPoints(rect)
        box = np.int_(box)
        boxes.append(box)
        cv2.drawContours(img, [box], 0, (0, 0, 255), 2)

#find boxes that are nearly in a straight line
left_points = []
right_points = []
for box in boxes:
    for point in box:
        if point[0] < img.shape[1] // 2:
            left_points.append(point)
        else:
            right_points.append(point)

#fit lines with scikitlearn RANSAC
def fit_line_ransac(points):
    if len(points) > 1:
        points = np.array(points)
        X = points[:, 0].reshape(-1, 1)
        y = points[:, 1]
        ransac = RANSACRegressor()
        ransac.fit(X, y)
        line_X = np.array([0, img.shape[1]])
        line_y_ransac = ransac.predict(line_X.reshape(-1, 1))
        return line_X, line_y_ransac
    return None, None

#left and right separately
left_line_X, left_line_y = fit_line_ransac(left_points)
right_line_X, right_line_y = fit_line_ransac(right_points)

if left_line_X is not None and left_line_y is not None:
    cv2.line(img, (int(left_line_X[0]), int(left_line_y[0])), (int(left_line_X[1]), int(left_line_y[1])), (0, 0, 255), 2)

if right_line_X is not None and right_line_y is not None:
    cv2.line(img, (int(right_line_X[0]), int(right_line_y[0])), (int(right_line_X[1]), int(right_line_y[1])), (0, 0, 255), 2)


cv2.imwrite('finalanswer.png', img)