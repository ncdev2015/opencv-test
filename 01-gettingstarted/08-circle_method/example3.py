import cv2
import numpy as np

Img = np.zeros((512, 512, 3), np.uint8)

window_name = 'Image'

center_coordinates = (220, 150)
radius = 100
color = (255, 133, 233)

thickness = -1

image = cv2.circle(Img, center_coordinates, radius, color, thickness)

cv2.imshow(window_name, image)
cv2.waitKey()
cv2.destroyAllWindows()