import cv2
import numpy as np

def empty(v):
    pass

img = cv2.imread('truth.PNG')
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

cv2.namedWindow('TrackBar')                     # 建立新視窗，作為HSV的控制面板
cv2.resizeWindow('TrackBar', 640, 320)

cv2.createTrackbar('Hue min', 'TrackBar', 0, 179, empty)       # 建立控制條(名稱、放置的視窗、初始值、最大值、函式)
cv2.createTrackbar('Hue MAX', 'TrackBar', 179, 179, empty)
cv2.createTrackbar('Sat min', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('Sat MAX', 'TrackBar', 255, 255, empty)
cv2.createTrackbar('Val min', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('Val MAX', 'TrackBar', 255, 255, empty)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)      # 就色彩空間來說，HSV比RGB更容易過濾顏色(根據像素點的色調、飽和度、亮度值高低進行篩選)

while True:
    h_min = cv2.getTrackbarPos('Hue min', 'TrackBar')           # 用While隨時取得控制條的值
    h_max = cv2.getTrackbarPos('Hue MAX', 'TrackBar')
    s_min = cv2.getTrackbarPos('Sat min', 'TrackBar')
    s_max = cv2.getTrackbarPos('Sat MAX', 'TrackBar')
    v_min = cv2.getTrackbarPos('Val min', 'TrackBar')
    v_max = cv2.getTrackbarPos('Val MAX', 'TrackBar')

    # print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(hsv, lower, upper)                        # 進行過濾(圖片、最小值、最大值)
    result = cv2.bitwise_and(img, img, mask=mask)                # 將每一個bit做and的運算，過濾出遮罩範圍內的顏色(原圖、原圖、遮罩)

    cv2.imshow('img', img)
    cv2.imshow('hsv', hsv)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)
    cv2.waitKey(1)

''' 黑色表示過濾掉的顏色，白色表示保留'''