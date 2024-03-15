import cv2
image = cv2.imread('bird.jpg')
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original', image)
cv2.imshow('Grey', grey)
cv2.waitKey(0)
cv2.destroyAllWindows()