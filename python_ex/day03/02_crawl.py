import requests
from bs4 import BeautifulSoup

url = "http://www.boannews.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36'}


req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, "lxml")

links = soup.find_all('a')
for link in links:
    print(f"{link.text} 링크 : {url}{link.get('href')}")
