import cv2
from cv2 import COLOR_BGR2GRAY
import numpy as np

img = cv2.imread('truth.PNG')
img = cv2.resize(img, (0,0), fx=0.4, fy=0.4)

''' 1. 圖片轉黑白 '''
# gray = cv2.cvtColor(img, COLOR_BGR2GRAY)
# cv2.imshow('gray', gray)

''' 2. 高斯濾波：去除高頻內容(雜訊、邊緣) '''
# blur = cv2.GaussianBlur(img, (15,15), 0)     # (圖片、高斯核(必為奇數)、標準差)
# cv2.imshow('blur', blur)

''' 3. 邊緣檢測：幫每一個像素打上分數(與周圍像素質的差異大小)，以此過濾出像素值高的邊緣部分 '''
canny = cv2.Canny(img, 200, 300)               # (圖片、最低門檻、最高門檻)：低於的忽略，高於的視為邊緣顯示
cv2.imshow('canny', canny)

''' 4. 膨脹：加粗線條 '''
dilate_kernel = np.ones((10,10), np.uint8)
dilate = cv2.dilate(canny, dilate_kernel, iterations=1)  # (圖片、核心(二維陣列)、膨脹次數)
cv2.imshow('dilate', dilate)

''' 5. 侵蝕：細縮線條 '''
erode_kernel = np.ones((10,10), np.uint8)
erode = cv2.erode(dilate, erode_kernel, iterations=1)
cv2.imshow('erode', erode)

cv2.imshow('test', img)
cv2.waitKey(0)