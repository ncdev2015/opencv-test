"""

Syntax: cv2.imread(path, flag)

Parameters:
path: A string representing the path of the image to be read.
flag: It specifies the way in which image should be read. It’s default value is cv2.IMREAD_COLOR

Return Value: This method returns an image that is loaded from the specified file.

"""

"""

All three types of flags are described below:

cv2.IMREAD_COLOR: It specifies to load a color image. Any transparency of image will be neglected. It is the default flag. Alternatively, we can pass integer value 1 for this flag.
cv2.IMREAD_GRAYSCALE: It specifies to load an image in grayscale mode. Alternatively, we can pass integer value 0 for this flag.
cv2.IMREAD_UNCHANGED: It specifies to load an image as such including alpha channel. Alternatively, we can pass integer value -1 for this flag.

"""