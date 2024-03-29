import cv2
import numpy as np

cap = cv2.VideoCapture(1) # or cap = cv2.VideoCapture(0) 



while True:
  im = cap.read()[1]
  im = cv2.flip(im,1)
  img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
  ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
  ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
  ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
  ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
  
  f1 = cv2.hconcat([thresh1,thresh2,thresh3])
  f2 = cv2.hconcat([thresh4,thresh5, img])
  f3 = cv2.vconcat([f1,f2])
  cv2.imshow("frame", f3)
  k = cv2.waitKey(1)
  if k == ord('q'):
    exit()
