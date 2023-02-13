import cv2

path = r'sample.png'

image = cv2.imread(path)

window_name = 'Image'

start_point = (100,50)
end_point = (125, 80)
color = (0,0,0) # black color
thickness = -1 # -1 will fill the entire shape

# Draw the rectangle
image = cv2.rectangle(image, start_point, end_point, color, thickness)

cv2.imshow(window_name, image)

cv2.waitKey(0)
cv2.destroyAllWindows()