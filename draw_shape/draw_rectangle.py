import cv2
import numpy as np

rekam = cv2.VideoCapture(2)
"""
Note : coordinate x = 640
	   coordinate y = 480
"""
x1 = int(640/2-20)
x2 = int(640/2+20)
y1 = int(480/2-20)
y2 = int(480/2+20)

while(1):
	ret, frame = rekam.read()
	frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
	cv2.imshow('rectangle', frame)
	if cv2.waitKey(1) == ord('q'):
		break
rekam.release()
cv2.destroyAllWindows()