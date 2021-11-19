import cv2
import numpy as np
from matplotlib import pyplot as plt
rekam = cv2.VideoCapture(2)
while(1):
	ret, frame = rekam.read()
	hsv = cv2.GaussianBlur(frame, (5, 5), 0)
	hsv = cv2.cvtColor(hsv, cv2.COLOR_BGR2HSV)
	lower_range = np.array([0, 160, 89])
	upper_range = np.array([41, 255, 255])
	mask = cv2.inRange(hsv, lower_range, upper_range)
	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	if cv2.waitKey(1) == ord('q'):
		break
cv2.destroyAllWindows()