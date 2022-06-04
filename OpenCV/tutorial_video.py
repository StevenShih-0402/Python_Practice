import cv2

cap = cv2.VideoCapture('Successful businessman is drinking water.mp4')     # 載入影片
# cap = cv2.VideoCapture(0)       # 載入鏡頭畫面(依鏡頭順序從0往下加)

while True:
    ret, frame = cap.read()  # 讀取影片的每一禎，回傳是否讀到下一張(ret/bool)和下一張圖片(frame)
    if ret:
        frame = cv2.resize(frame, (0,0), fx=0.45, fy=0.45)
        cv2.imshow('HOWHOW', frame)
    else:
        break
    if cv2.waitKey(10) == ord('q'):     # 若waitKey回傳Q的Unicode，break
        break