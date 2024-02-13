import cv2
import numpy as np

def draw(event,x,y,flags,param):
    print(x)
    print(y)
    pass

img =np.ones((512,512,3),np.uint8)

cv2.namedWindow("paint")


while(1):
    cv2.imshow("paint",img)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

cv2.destroyAllWindows()