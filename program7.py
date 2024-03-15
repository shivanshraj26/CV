import cv2
import numpy as np

image = np.zeros((500, 500, 3), dtype=np.uint8)
triangle_vertices = np.array([[250, 50], [50, 450], [450, 450]], dtype=np.int32)
cv2.polylines(image, [triangle_vertices], isClosed=True, color=(0, 255, 0), thickness=2)
centroid = np.mean(triangle_vertices, axis=0, dtype=np.int32)
cv2.circle(image, tuple(centroid), radius=5, color=(0, 0, 255), thickness=-1)
cv2.imshow("Triangle with Centroid", image)

def change_all_edges_color(event, x, y, flags, param):
    global image
    if event == cv2.EVENT_LBUTTONDOWN:
        new_color = np.random.randint(0, 256, 3).tolist()
        for i in range(len(triangle_vertices)):
            start_vertex = triangle_vertices[i]
            end_vertex = triangle_vertices[(i + 1) % len(triangle_vertices)]
            cv2.line(image, tuple(start_vertex), tuple(end_vertex), color=new_color, thickness=2)
        cv2.imshow("Triangle with Centroid", image)
cv2.setMouseCallback("Triangle with Centroid", change_all_edges_color)

while True:
    key = cv2.waitKey(1)# & 0xFF
    if key == ord('q'):
        break
cv2.destroyAllWindows()