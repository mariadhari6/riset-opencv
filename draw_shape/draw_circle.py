import cv2

rekam = cv2.VideoCapture(2)

x1 = int(640/2)
y1 = int(480/2)

while(1):
	ret, frame = rekam.read()
	frame = cv2.circle(frame, (x1, y1), 30, (0, 0, 255), -1)
	cv2.imshow('circle', frame)
	if cv2.waitKey(1) == ord('q'):
		break
rekam.release()
cv2.destroyAllWindows()