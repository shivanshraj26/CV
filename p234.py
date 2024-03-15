import cv2
import numpy as np
import math

cv2.namedWindow("Rotating 3D Cube", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Rotating 3D Cube", 600, 600)

cube_size = 75
#cube_color = (255, 0, 0)
edge_color = (255, 255, 255)
background_color = (0, 0, 0)
cube_thickness = 2

vertices = np.array([[-1, -1, -1],
                     [1, -1, -1],
                     [1, 1, -1],
                     [-1, 1, -1],
                     [-1, -1, 1],
                     [1, -1, 1],
                     [1, 1, 1],
                     [-1, 1, 1]], dtype=np.float32)

edges = [(0, 1), (1, 2), (2, 3), (3, 0),
         (4, 5), (5, 6), (6, 7), (7, 4),
         (0, 4), (1, 5), (2, 6), (3, 7)]

angle = 0

paused = False  

while True:
    if not paused :
        rotation_matrix = np.array([[math.cos(angle), -math.sin(angle), 0],
                                    [math.sin(angle), math.cos(angle), 0],
                                    [0, 1, 1]], dtype=np.float32) # [0, 0, 1]], dtype=np.float32) for square

        rotated_vertices = np.dot(vertices, rotation_matrix)

        projected_vertices = (rotated_vertices[:, :2] * cube_size + np.array([300, 300])).astype(int)

        frame = np.ones((600, 600, 3), dtype=np.uint8) * background_color

        for edge in edges:
            pt1 = tuple(projected_vertices[edge[0]])
            pt2 = tuple(projected_vertices[edge[1]])
            cv2.line(frame, pt1, pt2, edge_color, cube_thickness)

        cv2.imshow("Rotating 3D Cube", frame.astype(np.uint8))
    
        angle += 0.03 # comment this line to stop rotation
    key = cv2.waitKey(30)

    if key == ord('s'):
        paused = not paused
    elif key == ord('q'):
        break
    elif key == ord('p'):
        cube_size +=5
    elif key == ord('-'):
        cube_size -=5

cv2.destroyAllWindows()