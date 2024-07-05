from flask import Flask, render_template, request
import os
import openpyxl
import googletrans
import time
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index01.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    file = request.files["file"]
    file.save(os.path.join("uploads", file.filename))

    #엑셀 파일을 불러옴
    workbook = openpyxl.load_workbook(os.path.join("uploads", file.filename))
    sheet = workbook.active

    translator = googletrans.Translator()

    for row in sheet.iter_rows():
        for cell in row:
            translated_text = translator.translate(cell.value, dest='en').text
            cell.value = translated_text
            time.sleep(1)
    workbook.save('result_en.xlsx')
    
    return render_template('result.html')
    
# 이 조건문은 스크립트가 직접 실행될 때만 아래 코드를 실행도록 함
if __name__ == '__main__':
    app.run(debug=True)