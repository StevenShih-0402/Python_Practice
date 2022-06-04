#使用Action Chains模擬使用者動作

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys #可以讓我們輸入鍵盤資訊

PATH = "D:\Python練習檔\msedgedriver.exe"
driver = webdriver.Edge(PATH)
driver.get("https://popcat.click/")

action = ActionChains(driver)       #創建一個ActionChains物件(使用的瀏覽器)
action.key_down(Keys.F12)
action.key_up(Keys.F12)

for i in range(10000):
    action.perform()