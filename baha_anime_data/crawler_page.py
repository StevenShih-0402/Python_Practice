# 先爬取所有網頁的最後頁碼，若爬取不到就印出0

# 如果page = 0, continue

import requests
from bs4 import BeautifulSoup

# 建立 User-Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200',
}

tags = ["動作", "冒險", "奇幻", "異世界", "魔法", "超能力", "科幻", "機甲", "校園", "喜劇", "戀愛", "青春", "勵志", "溫馨", "悠閒", "料理", "親情", "感人", "運動", "競技", "偶像", "音樂", "職場", "推理", "懸疑", "時間穿越", "歷史", "戰爭", "血腥暴力", "靈異神怪", "黑暗", "特攝", "BL", "GL"]

print(len(tags))