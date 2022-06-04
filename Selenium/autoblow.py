#使用Action Chains模擬使用者動作

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = "D:\Python練習檔\msedgedriver.exe"
driver = webdriver.Edge(PATH)
driver.get("https://tsj.tw/")

blow = driver.find_element_by_id("click")                                               #『馬上吹』按鈕的id
blowCount = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[2]/h4[2]')   #取得次數的XPath(F12→對應的標籤→右鍵→複製→複製XPath)

items = []                                                                                                              #用來存放購買各個道具的動作
items.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[5]/button[1]'))     #『田字薯餅』的購買按鈕
items.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[5]/button[1]'))     #『電動飛機杯』的購買按鈕
items.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[5]/button[1]'))     #『田小班的Ban 10變身器』的購買按鈕

prices = []                                                                                                      #購買道具的價格
prices.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[4]'))       #『田字薯餅』的購買價格
prices.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[4]'))       #『電動飛機杯』的購買價格
prices.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[4]'))       #『田小班的Ban 10變身器』的購買價格

action = ActionChains(driver)       #創建一個ActionChains物件(使用的瀏覽器)
action.click(blow)                  #點擊『馬上吹』

for i in range(100000):
    action.perform()                #執行action裡面的動作(點擊『馬上吹』)
    count = int(blowCount.text.replace("您目前擁有", "").replace("技術點", ""))     #為了要買道具，需要用技術點的數字去和價格做比較，因此要將中文替換掉，並轉成int
    for j in range(3):
        price = int(prices[j].text.replace("技術點", ""))                            #將所需技術點去掉中文並轉成int
        if(price <= count):
            upgrade = ActionChains(driver)                                          #創建一個ActionChains物件，紀錄購買動作
            upgrade.move_to_element(items[j])                                       #滑鼠移到購買按鈕上
            upgrade.click()                                                         #按下購買
            upgrade.perform()                                                       #執行！
            break                                                                   #買完就要break，否則會一直買