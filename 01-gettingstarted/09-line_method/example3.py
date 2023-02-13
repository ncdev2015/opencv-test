import cv2
import numpy as np

Img = np.zeros((512, 512, 3), dtype = 'uint8')

window_name = 'Image'

start_point = (100,100)
end_point = (450, 450)
color = (255, 255, 255)
thickness = 9

image = cv2.line(Img, start_point, end_point, color, thickness)

cv2.imshow('Drawing_Line', image)
cv2.waitKey()
cv2.destroyAllWindows()