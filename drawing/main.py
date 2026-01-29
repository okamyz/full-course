import os

import cv2

img = cv2.imread(os.path.join('.', 'drawing', 'whiteboard.jpg'))

img = cv2.resize(img, (975, 622))

print(img.shape)

# line
cv2.line(img, (100, 150), (400, 170), (0, 255, 0), 5) # rumusnya cv2.lin(media, point1, point2, warna, ketebalan)

# rectangle
cv2.rectangle(img, (500, 100), (700, 300), (255, 0, 0), -1) # rumusnya cv2.rectangle(media, pojok_kiri_atas, pojok_kanan_bawah, warna, ketebalan)

# circle
cv2.circle(img, (500, 450), 80, (0, 0, 255), 10) # rumusnya cv2.circle(media, center, radius, warna, ketebalan)

# text
cv2.putText(img, 'You have no enemies', (175, 311), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 5) # rumusnya cv2.putText(media, text, posisi, font, ukuran_font, warna, ketebalan)

cv2.imshow('img', img)
cv2.waitKey(0)
