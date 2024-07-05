import requests
from bs4 import BeautifulSoup

# URL 설정
url = "https://www.malware-traffic-analysis.net/2023/index.html"
headers = {
    'User-Agent': 'Mozilla/5.0',
    'Content-Type': 'text/html; charset=utf-8'
}

# 요청 보내기
req = requests.get(url, headers=headers)
# BeautifulSoup로 HTML 파싱
soup = BeautifulSoup(req.text, "lxml")

results=[]
# 제목과 링크 추출
tags = soup.select("#main_content > div.content > ul > li > a.main_menu")
# 결과 출력
for tag in tags: 
    title = tag.get_text()
    link = "https://www.malware-traffic-analysis.net/2024/" + tag['href'] 
    results.append(f"Title: {title}\nURL: {link}\n")

with open('malwares.txt','w',encoding='utf-8') as file:
    for result in results:
        file.write(result)


