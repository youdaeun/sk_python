import feedparser

url = "http://www.boannews.com/media/news_rss.xml?mkind=1"

feed= feedparser.parse(url)
for entry in feed.entries:
    print(entry.title)
    print(entry.link)
    print(entry.description)
    print(entry.author)