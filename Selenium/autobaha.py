import time
from selenium import webdriver                  #將selenium模組中的webdriver方法import進來(這樣寫就不會將整個selenium給import進來)               
from selenium.webdriver.common.keys import Keys #可以讓我們輸入鍵盤資訊

from selenium.webdriver.common.by import By     #selenium中為了執行等待的動作，需要import的方法
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = "D:/Python練習檔/msedgedriver.exe"       #瀏覽器的webdriver位置(這裡用的是Edge的webdriver)

driver = webdriver.Edge(PATH)                   #用Edge瀏覽器執行webdriver
driver.get("https://forum.gamer.com.tw/")       #打開網址所屬的網頁

search = driver.find_element_by_name("search")    #尋找巴哈搜尋欄的name標籤，存到search變數
search.clear()                                    #清空搜尋欄
search.send_keys("")                              #輸入文字(要搜尋的內容)
search.send_keys(Keys.RETURN)                     #輸入enter鍵(RETURN)

WebDriverWait(driver, 10).until(                                #載入需要時間，且會因不同裝置而速度不同，如果在頁面還沒載入就執行動作，可能會造成執行上的錯誤(抓不到資料之類的)
    EC.presence_of_element_located((By.ID, "resInfo-3"))        #這裡的意思是：瀏覽器會等到id=resInfo-3的標籤(此處指巴哈搜尋時間的回報文字)載入完成後再執行動作，最多等10秒
)

titles = driver.find_elements_by_css_selector("a.gs-title")     #尋找標題的class標籤
for title in titles:                                        #用迴圈一個一個印出來
    print(title.text)

print(driver.title)                             #印出網頁標題(<title>)

link = driver.find_element_by_link_text("")     #將指令(尋找標籤內文字)存入變數link(此處選取要點開的超連結)
link.click()                                    #點擊link
driver.back()                                   #讓瀏覽器回到上一頁
driver.back()
driver.forward()                                #讓瀏覽器前往下一頁

time.sleep(10)
driver.quit()                                   #關閉(離開)瀏覽器