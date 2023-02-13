import cv2

path = r'sample.png'
image = cv2.imread(path, 0) # Reading image in a grayscale mode

window_name = 'image'
cv2.imshow(window_name, image)

cv2.waitKey(0)
cv2.destroyAllWindows()