'''
---準備人臉辨識模型---

去OpenCV的Github找到資料夾Data 
→ 資料夾haarcascades 
→ frontaiface_default的檔案 
→ 點選Raw後全選複製 
→ 建立新檔案face_detect.xml，貼上。

'''

import cv2

img = cv2.imread('lenna.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('face_detect.xml')
facerect = face_cascade.detectMultiScale(img_gray, 1.1, 3)

for (x,y,w,h) in facerect:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

'''
(圖片、縮小倍率、精確度(臉部須被偵測次數))
---人臉辨識大致上的運作流程---

1.透過一個小方格，逐一掃視整張圖片，看有沒有偵測到人臉，有偵測到就會記錄下來
2.偵測完一輪後，將圖片縮小，再檢測一輪
3.最後回傳一個代表臉部範圍的矩形資訊(x,y,w,h)
'''

cv2.imshow('img', img)
cv2.waitKey(0)