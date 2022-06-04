from flask import Flask

app = Flask(__name__)           #建立一個應用程式的物件，__name__是python內建變數，代表目前執行的模組

@app.route("/")                 #函式的裝飾(decorator)，以下面的函式為基礎，提供附加的功能，route表示我們要處理的網站路徑，此處的斜線表示根目錄
def home():
    return "Hello Flask!"       #使用者連線到根目錄時，要執行home，並回傳Hello Flask!

@app.route("/test")
def test():
    return "Test Flask(^O^)"

if(__name__ == "__main__"):     #如果以主程式去執行
    app.run()                   #就立刻啟動伺服器

# 這樣就完成了一支最基本的網頁程式
# 此程式必須24小時不間斷執行，否則網頁將無法顯示內容

#127.0.0.1:5000/test
#   (主機名稱) / (目錄)

# 網站壞掉：伺服器無法(拒絕)連線
# Not Found：程式沒有處理連線(目錄不存在)


# -----------------------------------------------------------------

#上傳到Heroku雲端主機：
# 成功以後，會給你一串網域名稱，就能將你的網站放上去，讓別人搜尋到

# 步驟：
# 1.建立一個Flask專案描述檔案
    # runtime.txt: 描述使用的python版本
    # requirements.txt: 描述程式需使用的套件
    # Procfile: 描述Heroku要如何執行程式
# 2.安裝git
# 3.註冊Heroku帳號，點選create new app
# 4.安裝Heroku的CLI(命令列)工具
# 5.將程式部屬到Heroku App(用命令列執行)
    # 登入Heroku
        # heroku login
    # 初始化專案    
        # git init
        # heroku git:remote -a 專案名稱
    # 更新專案
        # git add .
        # git commit -m "更新的訊息"
        # git push heroku master

