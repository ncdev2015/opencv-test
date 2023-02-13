import cv2

path = r'sample.png'

image = cv2.imread(path)

window_name = 'Image'

center_coordinates = (120, 50)
radius = 20

color = (255, 0, 0)

thickness = 2

image = cv2.circle(image, center_coordinates, radius, color, thickness)

cv2.imshow(window_name, image)

cv2.waitKey()
cv2.destroyAllWindows()