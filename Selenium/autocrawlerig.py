from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import wget

PATH = "D:\Python練習檔\msedgedriver.exe"
driver = webdriver.Edge(PATH)
driver.get("https://www.instagram.com/")

#---1.輸入帳號、密碼，按下Enter---
username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)

password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)

login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')

username.clear()
password.clear()

username.send_keys("")      #帳號
password.send_keys("")      #密碼

login.click()

#---2.搜尋標籤---
search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))
)

keyword = ""                        #要搜尋的關鍵字
search.send_keys(keyword)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)
search.send_keys(Keys.RETURN)       #IG的搜尋比較特殊，要有間隔的按兩下Enter才可以搜尋

#---3.抓取圖片---
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "FFVAD"))
)

for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")        #執行JS程式碼，讓頁面滑到最底層顯示更多貼文
    time.sleep(3)

path = os.path.join(keyword)        #創建資料夾路徑(資料夾名稱)
os.mkdir(path)

imgs = driver.find_elements_by_class_name("FFVAD")
count = 0

for img in imgs:
    save = os.path.join(path, keyword + str(count) + '.jpg')        #, 檔名格式
    wget.download(img.get_attribute("src"), save)                   #下載位置, 要存取的位置
    count += 1


