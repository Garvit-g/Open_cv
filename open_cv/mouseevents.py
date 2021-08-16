import cv2
import numpy as np


def draw_rectangle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.rectangle(img,(x,y),(x+150,y+150),(0,0,255),15)
        print("Point Clicked: x {} y {}".format(x,y))


img=cv2.imread('penguin.jpeg',1)  


cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_rectangle) 

while True :
    cv2.imshow('image',img)
    if cv2.waitKey(1)  == ord('q'):
        break
cv2.destroyAllWindows()