import cv2
import os

image_path = r'/home/usuario/Projects/PythonApps/opencv-test/01-gettingstarted/03-writing-a-image/sample.png'
directory = r'/home/usuario/Projects/PythonApps/opencv-test/01-gettingstarted/03-writing-a-image'

img = cv2.imread(image_path)
os.chdir(directory)

print("Before saving image:")
print(os.listdir(directory))

filename = "savedImage.jpg"
cv2.imwrite(filename, img)

print("After saving image:")
print(os.listdir(directory))

print("Successfully saved")	