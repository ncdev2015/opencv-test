import cv2

path = r'sample.png'

img = cv2.imread(path, 0) # grayscale flag

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()