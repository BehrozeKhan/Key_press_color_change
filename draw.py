import numpy as np
import cv2

print("Color Changing by Keyboard buttons")
canvas = np.ones([500,500,3], 'uint8')*255
radius = 10
color = (0,0,0)
pressed = False

def click(event , x , y , flags , param):
	global canvas,pressed

	if event == cv2.EVENT_LBUTTONDOWN:
		pressed = True
		cv2.circle(canvas,(x,y), radius, color, -1)
	elif event == cv2.EVENT_MOUSEMOVE and pressed == True:
		cv2.circle(canvas,(x,y),radius, color, -1)
	elif event == cv2.EVENT_LBUTTONUP:
		pressed = False

cv2.namedWindow("Canvas")
cv2.setMouseCallback("Canvas",click)

while True:
	cv2.imshow("Canvas",canvas)

	ch = cv2.waitKey(1)
	if ch == ord('g'):
		color = (0,255,0)
	elif ch == ord('b'):
		color = (255,0,0)
	elif ch == ord('r'):
		color = (0,0,255)
	elif ch == ord('q' and 'w'):
		break
