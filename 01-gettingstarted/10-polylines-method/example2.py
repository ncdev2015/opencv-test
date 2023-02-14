import cv2
import numpy as np

path = r'sample.png'
image = cv2.imread(path)

window_name = 'Image'
pts = np.array([[25, 70], [25, 145],
                [75, 190], [150, 190],
                [200, 145], [200, 70],
                [150, 25], [75, 25]],
               np.int32)

pts = pts.reshape((-1, 1, 2))
isClosed = True
color = (0, 255, 0)
thickness = 8

image = cv2.polylines(image, [pts], isClosed, color, thickness)

while(1):
    cv2.imshow('image', image)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()