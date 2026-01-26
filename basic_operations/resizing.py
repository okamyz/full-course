# resizing
import os 

import cv2


img = cv2.imread(os.path.join('.', 'basic_operations', 'sonic.jpg'))

resized_img = cv2.resize(img, (368, 368)) # in this code the input size is (width, height)

# but in numpy the shape is (height, width, channels) dont forget it
print(img.shape)
print(resized_img.shape)

cv2.imshow('img', img)
cv2.imshow('resized_img', resized_img)
cv2.waitKey(0)