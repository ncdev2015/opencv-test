import cv2

path = r'sample.png'

image = cv2.imread(path, 0)
window_name = 'Image'

start_point = (225,0)
end_point = (0, 225)
color = (0, 0, 0)
thickness = 5

image = cv2.line(image, start_point, end_point, color, thickness)

cv2.imshow(window_name, image)
cv2.waitKey()
cv2.destroyAllWindows()