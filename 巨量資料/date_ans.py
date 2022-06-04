import datetime

# #  取得今日的日期
today = datetime.date.today()
print(today)

# # 直接設定日期
new_year = datetime.date(2020, 10, 10)
print(new_year)

# # 直接設定時間
noon = datetime.time(13, 14, 20)
print(type(noon))
print(noon)

# #  取得此時此刻的 日期+時間
now = datetime.datetime.now()
week = 3
print(now)
print("現在時刻:{} 星期{}".format(now, week))
print("現在時刻:%s 星期%d" % (now, week))

## 將日期 轉為指定顯示的文字格式
Time_obj = datetime.datetime.now()
Time_str = Time_obj.strftime("%Y/%m/%d")  # 將要的年月日轉為字串
print(Time_str)
print(type(Time_str))

# # # 參照上面範例 從現在的時間(datetime.datetime.now())取出指定的時間格式  EX:09:15:50
Time_obj = datetime.datetime.now()
Time_str = Time_obj.strftime("%H:%M:%S")
print(Time_str)

# #文字轉時間 #請將millenium_turn 填完整
Time_str="2020-09-17 11:05:33"
millenium_turn = datetime.datetime.strptime(Time_str,"%Y-%m-%d %H:%M:%S")
print("現在時刻:%s" % millenium_turn)

## 自我練習