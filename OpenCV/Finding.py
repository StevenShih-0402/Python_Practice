import cv2

img = cv2.imread('shape.jpg')
img_contours = img.copy()

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)     # 輪廓檢測不需要顏色
canny = cv2.Canny(img, 150, 200)                # 用Canny找出圖形邊緣

''' 
    輪廓檢測：findContours(圖片、內/外/內外輪廓、壓縮水平/垂直/不壓縮輪廓點)
    執行後回傳2個參數：輪廓(紀錄X、Y座標的陣列/contours)和階層(hierarchy)
'''
contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for cnt in contours:
    '''
    1.畫出找到的輪廓
        (畫布、找到的輪廓、要畫幾個輪廓(全畫輸入-1)、顏色、粗細)
    '''
    cv2.drawContours(img_contours, cnt, -1, (0, 255, 0), 3)
    
    '''
    2.輪廓內的面積
        (如果輸出有0不用慌張，只是雜訊而已)
    '''
    area = cv2.contourArea(cnt)
    print('Area = ' + str(area))

    '''
    3.輪廓的周長
        (輪廓參數、輪廓是否閉合)
    '''
    length = cv2.arcLength(cnt, True)
    print('Length = ' + str(length))

    '''
    4.輪廓的頂點
        (輪廓參數、近似值(越高偵測出的邊數越多)、輪廓是否閉合)
    '''
    vertices = cv2.approxPolyDP(cnt, length*0.02, True)
    corner = len(vertices)
    print(corner)

    '''
    5.用矩形將所有圖形框出來
    '''
    if area > 500:                                                        # 篩掉雜訊(回傳值為0的資訊)
        x, y, w, h = cv2.boundingRect(vertices)                           # 回傳左上角的X、Y座標和矩形的長寬
        cv2.rectangle(img_contours, (x, y), (x+w, y+h), (0,0,255), 4)     # 畫出矩形

        '''
        6.根據頂點數量判斷圖形類別，並加上文字
        '''
        if corner == 3:
            cv2.putText(img_contours, 'triangle', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
        elif corner == 4:
            cv2.putText(img_contours, 'rectangle', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
        elif corner == 5:
            cv2.putText(img_contours, 'pentagon', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
        elif corner >= 6:
            cv2.putText(img_contours, 'circle', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)


cv2.imshow('img', img)
cv2.imshow('canny', canny)
cv2.imshow('img_contours', img_contours)
cv2.waitKey(0)

