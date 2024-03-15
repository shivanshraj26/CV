import cv2
import numpy as np
image = np.zeros((400, 400, 3))
cv2.rectangle(image, (50, 50), (150, 150), (255, 0, 0), -1)
cv2.circle(image, (300, 100), 50, (0, 255, 0), -1)
cv2.line(image, (250, 150), (350, 50), (0, 0, 255), 3)
cv2.imshow('Original 2D Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()