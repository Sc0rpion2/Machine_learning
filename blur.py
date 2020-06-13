#!/usr/bin/env python3

import numpy as np
import cv2

img = cv2.imread('images/faces.jpg', 0)
ims = cv2.resize(img, (740, 940))
cv2.imshow('image', ims)
cv2.waitKey(0)
cv2.destroyAllWindows()

faces = faceCascade.detectMultiScale(
  gray,
  scaleFactor=1.1,
  minNeighbors=5,
  minSize=(30, 30),
  flags = cv2.cv.CV_HAAR_SCALE_IMAGE

)
