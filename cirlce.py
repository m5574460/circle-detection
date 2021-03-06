import cv2
import numpy as np

image = cv2.imread("C:/Users/User/Desktop/circle/image/coins.png")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (11, 11), 0)

canny = cv2.Canny(blurred, 30, 150)
#canny_dilate = cv2.dilate(canny, None, iterations=1)
#canny_erode = cv2.erode(canny_dilate, None, iterations=1)

(_, cnts, _) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("I count {} coins in this image". format(len(cnts)))

contours = image.copy()
cv2.drawContours(contours, cnts, -1, (0, 255, 0), 2)

# loop over the contours individually
centroid = image.copy()
for c in cnts:
	# Area
    print(cv2.contourArea(c))
    # perimeter
    print(cv2.arcLength(c,True))

	# centroid from moments
    M = cv2.moments(c)
    cx = int(M["m10"]/M["m00"])
    cy = int(M["m01"]/M["m00"])

    cv2.circle(centroid, (cx, cy), 5, (0, 0, 255), -1)

result = np.hstack([contours, centroid])
cv2.imshow("Result:", result)
cv2.waitKey(0)