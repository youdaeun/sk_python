from flask import Flask, render_template, request
import feedparser

app = Flask(__name__)

# @app.route("/")는 데코레이터로, 
# URL 경로 '/'에 접근할 때 이어지는 함수를 호출하도록 지정
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rss', methods=['GET', 'POST'])
def rss():
    rss_url = request.form['rss_url']
    feed = feedparser.parse(rss_url)
    return render_template('rss.html', feed=feed)

# 이 조건문은 스크립트가 직접 실행될 때만 아래 코드를 실행도록 함
if __name__ == '__main__':
    app.run(debug=True)