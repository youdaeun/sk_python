import os, time, re
from datetime import datetime
DIR_PATH= 'static'

#현재 시간 표시
now = datetime.now()
day = now.strftime("%Y-%m-%d")
hour = now.strftime("%H:%M:%S")

#정규 표현식 - 이메일 탐지
email_pattern = re.compile(r'[\w\.-]+@[\w\.-]+')
jumin_pattern = re.compile(r'\d{6}[-]\d{7}')

pre_file = set(os.listdir(DIR_PATH))

while True:
    cureent_file = set(os.listdir(DIR_PATH))
    result_diff = cureent_file - pre_file
    
    for file_name in result_diff:
        print(f"새로운 파일 탐지 : {file_name}")
        with open(f"{day}월_탐지 보고서.txt", "a", encoding="UTF-8") as file:
            file.write(f"작성자: 조정원\n")
            file.write(f"주요 내용: 신규 파일 탐지\n")
            file.write(f"시간: {hour} 파일 내용 {file_name}\n")
            
        #파일의 내용을 확인하기
        file_path = os.path.join(DIR_PATH, file_name)

        with open(file_path, "r", encoding="UTF-8") as file:
            lines = file.readlines()
            for num, line in enumerate(lines):
                if line.startswith(("#","//")):
                    print(f"주석처리: {num}번째줄 : {line}")
                #이메일 탐지
                emails = email_pattern.findall(line)
                for email in emails:
                    print(f"이메일 {num}번째줄: {email}")
                #주민번호 탐지
                jumins = jumin_pattern.findall(line)
                for jumin in jumins:
                    print(f"주민번호 {num}번째줄: {jumin}")

    pre_file = cureent_file
    print("확인!!")
    time.sleep(1)