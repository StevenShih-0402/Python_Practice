# 在Python，陣列是numpy裡的方法之一
# 每張圖片都是一組一組的RGB陣列，組成多維陣列呈現出來

import random
import cv2
import numpy as np

''' 1.自製圖片：創建一個多維陣列(300/長，300/寬，3/RGB)，裡面的值為0~255(8bits表示) '''
# img = np.empty((300,300,3), np.uint8)   

'''
    大概長這樣：
    [
        [[255,255,255],[0,0,0],...]
        [[255,255,255],[0,0,0],...]
        ...
    ]
    [
        [[255,255,255],[0,0,0],...]
        [[255,255,255],[0,0,0],...]
        ...
    ]
'''

''' 2.隨機改變「300*圖片寬」範圍內的像素 '''
img = cv2.imread('truth.PNG')
# for row in range(300):
#     for col in range(img.shape[1]):
#         img[row][col] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]   #[B，G，R]
cv2.imshow('test', img)

''' 3.切割圖片(依座標軸切割) '''
newImg = img[:600, 300:500]  # [Y起點:Y終點，X起點:X終點]
cv2.imshow('split_img', newImg)

cv2.waitKey(0)