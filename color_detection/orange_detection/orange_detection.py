import cv2
import numpy as np

gambar = cv2.imread('jeruk.jpeg')

hsv = cv2.cvtColor(gambar, cv2.COLOR_BGR2HSV)
lower_range = np.array([3, 42, 56], dtype=np.uint8)
upper_range = np.array([41,  240, 255], dtype=np.uint8)
mask = cv2.inRange(hsv, lower_range, upper_range)

cv2.imshow('mask', mask)
cv2.imshow('image', gambar)

while(1):
	if cv2.waitKey(0) == ord('q'):
		break
cv2.destroyAllWindows()