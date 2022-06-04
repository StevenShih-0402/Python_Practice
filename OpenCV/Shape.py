import cv2
import numpy as np

img = np.zeros((600,600,3), np.uint8)       # 創建值為0的陣列

''' 1. 直線 '''
cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0,255,0), 3)        # 畫布、起點、終點、顏色(RGB)、粗細

''' 2. 正方形 '''
cv2.rectangle(img, (0,0), (100,150), (255,0,0), cv2.FILLED)             # 畫布、左上角、右下角、顏色(RGB)、粗細(填滿)        

''' 3. 圓形 '''
cv2.circle(img, (300,300), 15, (0,0,255), 2)                            # 畫布、圓心、半徑、顏色、粗細

''' 4. 文字 '''
cv2.putText(img, 'Hello', (100,500), cv2.FONT_HERSHEY_PLAIN, 6, (87,63,74), 3)  # 畫布、內文、位置(左下角)、字體、大小、顏色、粗細 (不支援中文)

cv2.imshow('black', img)
cv2.waitKey(0)