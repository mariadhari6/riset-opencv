import cv2

gambar = cv2.imread('anime.jpg')
cv2.imshow('anime', gambar)
while (1):
	tombol = cv2.waitKey(0)
	if tombol == 27:
		break
cv2.destroyAllWindows()