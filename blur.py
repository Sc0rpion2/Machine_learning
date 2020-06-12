#!/usr/bin/env python3


import cv2


img = cv2.imread('images/faces.jpg', 0)
ims = cv2.resize(img, (740, 940))
cv2.imshow('image', ims)
cv2.waitKey(0)
cv2.destroyAllWindows()
