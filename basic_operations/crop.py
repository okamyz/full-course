# crop
import os

import cv2

img = cv2.imread(os.path.join('.', 'basic_operations', 'sonic.jpg'))

print(img.shape)

cropped_img = img[145:590, 145:590]

cv2.imshow('img', img)
cv2.imshow('cropped_img', cropped_img)
cv2.waitKey(0)