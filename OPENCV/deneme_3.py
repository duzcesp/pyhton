import cv2
import random

img=cv2.imread('indir.jpg',-1)

tag = img[50:70, 60:90]
img[10:30, 65:95]=tag





cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()