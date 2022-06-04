from openpyxl import Workbook, load_workbook

wb = Workbook()                     # 新的Excel檔案
ws = wb.active
ws.title = "B1111"                  # 工作表名稱

ws.append([123,456,789,12,345])     # 新增橫排資料
ws.append([123,456,789,12,345])
ws.append([123,456,789,12,345])

wb.save("Creater.xlsx")             # 要儲存的檔名