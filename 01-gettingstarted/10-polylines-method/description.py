"""

cv2.polylines() method is used to draw a polygon on any image.
--------------------------------------------------------------

Syntax: cv2.polylines(image, [pts], isClosed, color, thickness)

Parameters:
	image: It is the image on which circle is to be drawn.
	pts: Array of polygonal curves.
	npts: Array of polygon vertex counters.
	contours: Number of curves.
	isClosed: Flag indicating whether the drawn polylines are closed or not. If they are closed, the function draws a line from the last vertex of each curve to its first vertex. 
	color: It is the color of polyline to be drawn. For BGR, we pass a tuple.
	thickness: It is thickness of the polyline edges.

	Return Value: It returns an image.

"""