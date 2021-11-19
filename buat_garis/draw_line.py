import cv2
import numpy as np
import random

x1 = random.randint(0, 600)
x2 = random.randint(0, 600)
y1 = random.randint(0, 600)
y2 = random.randint(0, 600)

k = [x1, y1, x2, y2]
img = np.zeros((600, 600, 3), np.uint8)
"""
np.zeros adalah fungsi untuk
Membuat koordinat kartesius dengan x=600, y=600
"""

garis = cv2.line(img, (k[0], k[1]), (k[2], k[3]), (0, 0, 255), 3)
cv2.imshow('garis', garis)
cv2.waitKey(0)
cv2.destroyAllWindows()