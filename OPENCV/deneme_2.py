import cv2
import random


img = cv2.imread('indir.jpg',-1)
img = cv2.resize(img,(0,0),fx=3,fy=3)

for i in range(300):
    for j in range(img.shape[1]):
        img[i][j]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

