import os
import time
import re
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication 
from dotenv import load_dotenv

# 사용자 정의 함수 - 메일 보내기 mail_sender
def mail_sender(file_path, line):
    load_dotenv()
    SECRET_ID = os.getenv("SECRET_ID")
    SECRET_PASS = os.getenv("SECRET_PASS")

    smtp = smtplib.SMTP('smtp.naver.com', 587)
    smtp.ehlo()
    smtp.starttls()

    smtp.login(SECRET_ID, SECRET_PASS)
    send_email = "youremail"
    recv_email ="youremail"

    text = f"탐지라인: {line}"

    # MIMEMultipart 객체 생성
    msg = MIMEMultipart()
    msg['Subject'] = f"모니터 탐지: {file_path}"  
    msg['From'] = send_email          
    msg['To'] = recv_email            

    contentPart = MIMEText(text, 'plain', 'utf-8')
    msg.attach(contentPart) 

    etc_file_path = r'006.txt'
    with open(etc_file_path, 'rb') as f : 
        etc_part = MIMEApplication(f.read())
        etc_part.add_header('Content-Disposition', 'attachment', filename=etc_file_path)
        msg.attach(etc_part)

    smtp.sendmail(send_email, recv_email, msg.as_string())
    smtp.quit()

DIR_PATH = 'static'

# 현재 시간 표시
now = datetime.now()
day = now.strftime("%Y-%m-%d")
hour = now.strftime("%H:%M:%S")

# 정규 표현식 - 이메일 탐지
email_pattern = re.compile(r'[\w\.-]+@[\w\.-]+')
jumin_pattern = re.compile(r'\d{6}[-]\d{7}')

# 현재 작업 디렉토리 출력
print("현재 작업 디렉토리:", os.getcwd())

# DIR_PATH가 존재하는지 확인하고, 존재하지 않으면 생성합니다
if not os.path.exists(DIR_PATH):
    os.makedirs(DIR_PATH)

pre_file = set(os.listdir(DIR_PATH))

while True:
    current_file = set(os.listdir(DIR_PATH))
    result_diff = current_file - pre_file
    
    for file_name in result_diff:
        print(f"새로운 파일 탐지: {file_name}")
        with open(f"{day}월_탐지 보고서.txt", "a", encoding="UTF-8") as file:
            file.write(f"작성자: 조정원\n")
            file.write(f"주요 내용: 신규 파일 탐지\n")
            file.write(f"시간: {hour} 파일 내용 {file_name}\n")
            
        # 파일의 내용을 확인하기
        file_path = os.path.join(DIR_PATH, file_name)

        with open(file_path, "r", encoding="UTF-8") as file:
            lines = file.readlines()
            for num, line in enumerate(lines):
                if line.startswith(("#", "//")):
                    print(f"주석처리: {num}번째 줄: {line}")
                    mail_sender(file_path, line)
                # 이메일 탐지
                emails = email_pattern.findall(line)
                for email in emails:
                    print(f"이메일 {num}번째 줄: {email}")
                # 주민번호 탐지
                jumins = jumin_pattern.findall(line)
                for jumin in jumins:
                    print(f"주민번호 {num}번째 줄: {jumin}")

    pre_file = current_file
    print("확인!!")
    time.sleep(1)
