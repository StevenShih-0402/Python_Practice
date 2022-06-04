import cv2

img = cv2.imread('truth.PNG')                     # 讀取圖檔(無法讀取中文檔名)

img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)     # 改變圖片大小(檔名、長寬(0表示不變)、倍數縮放)
cv2.imshow('education',img)                       # 顯示圖片(視窗標題、檔案變數)
cv2.waitKey(0)                                    # 等待5000毫秒後關閉，輸入0表示無限等待，直到鍵盤被按下任意鍵，或是關閉視窗，才會回傳按鍵編號結束

