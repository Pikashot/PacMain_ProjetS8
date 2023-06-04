import cv2
import numpy as np

cv2.namedWindow("Window")

while True:
    key = cv2.waitKeyEx(1)
    if key != -1:
        print(key)
