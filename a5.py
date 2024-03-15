import cv2
import numpy as np
image = cv2.imread('bird.jpg')
kernel = np.ones((3,3), dtype=np.uint8)
eroded = cv2.erode(image, kernel, iterations=5)
dialate = cv2.dilate(image, kernel, iterations=5)
cv2.imshow('Original', image)
cv2.imshow('Eroded', eroded)
cv2.imshow('Dialated', dialate)
# resize=cv2.resize(image, (250,250))
# cv2.imshow('Original', resize)
cv2.waitKey(0)
cv2.destroyAllWindows()