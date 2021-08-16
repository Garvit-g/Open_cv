import numpy as np
import cv2

img = cv2.imread('penguin.jpeg',cv2.IMREAD_COLOR)
cv2.line(img,(150,150),(300,300),(255,255,255),15)
cv2.rectangle(img,(150,25),(300,150),(0,0,255),15)
cv2.circle(img,(100,63), 55, (0,255,0), -1)
pts = np.array([[100,50],[200,300],[700,200],[500,100]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255), 3)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Garvit was here!',(10,500), font, 2, (0,0,0), 5, cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()