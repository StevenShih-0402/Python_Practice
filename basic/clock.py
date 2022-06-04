from tkinter import *           #(Tk interface), 是python內建的應用程式介面套件      
from tkinter.ttk import *       #ttk(Themed Tkinter)，意指主題化版本，是tkinter美化元件外觀的模組

from time import strftime       #用於顯示當地時間

root = Tk()                   #建立應用程式視窗
root.title("Clock")

def time():
    string = strftime("%H:%M:%S %p")        #時間格式
    label.config(text = string)             #confit用於修改介面格式(像是text、fg(foreground)...)，此處用於將文字內容修改成string
    label.after(1000, time)                 #定時器，1秒後執行函數time


label = Label(root, font=("Stick", 80), background="black", foreground="#00d2d3")
label.pack(anchor="center")     #讓Label剛好被視窗包覆並置中

time()

mainloop()                      #Tkinter的訊息迴圈，在視窗關閉前，程式碼會不斷在這個迴圈裡運行