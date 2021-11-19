import cv2
from matplotlib import pyplot as plt
rekam = cv2.VideoCapture(2)

while(1):
	ret, frame = rekam.read()
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) == ord('q'):
		break
frame.release()
cv2.destroyAllWindows()