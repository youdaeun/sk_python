#pip install feedparser
#pip install openpyxl

import feedparser
from openpyxl import Workbook

url = "https://www.dailysecu.com/rss/allArticle.xml"

feed = feedparser.parse(url)
titles = []
links = []
descriptions = []
authors = []
pubDates = []

for entry in feed.entries:
    titles.append(entry.title)
    links.append(entry.link)
    descriptions.append(entry.description)
    authors.append(entry.author)
    pubDates.append(entry.published)

# 워크북과 워크시트를 생성합니다.
wb = Workbook()
ws = wb.active
ws.title = "RSS Feed Data"

# 첫 번째 행에 헤더를 작성합니다.
headers = ['Title', 'Link', 'Description', 'Author', 'Published']
ws.append(headers)

# 데이터를 행 단위로 작성합니다.
for i in range(len(titles)):
    ws.append([titles[i], links[i], descriptions[i], authors[i], pubDates[i]])

# 엑셀 파일로 저장합니다.
wb.save('result.xlsx')
