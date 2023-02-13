import cv2

path = r'sample.png'
image = cv2.imread(path)

window_name = "Image"

text = "GeeksforGeeks"
font = cv2.FONT_HERSHEY_SIMPLEX

org = (00,185)
fontScale = 1
color = (0, 0, 255)
thickness = 2

image = cv2.putText(image, text, org, font, fontScale, color, thickness, cv2.LINE_AA, False)
  
image = cv2.putText(image, text, org, font, fontScale, color, thickness, cv2.LINE_AA, True) 

cv2.imshow(window_name, image)

cv2.waitKey()
cv2.destroyAllWindows()