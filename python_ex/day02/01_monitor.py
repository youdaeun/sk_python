#특정 디렉터리를 모니터링 - 파일 정보들을 수집
#새로운 파일이 업로드가 되면, 기존 파일 정보들과 비교!!!
#관리자 페이지 아이디 admin / admin
#pre_file - new_file 목록을 차이점!
#비교한 결과 새롭게 추가된 파일을 리스트화!!

import os, time
from datetime import datetime
DIR_PATH= 'static'

#현재 시간 표시
now = datetime.now()
day = now.strftime("%Y-%m-%d")
hour = now.strftime("%H:%M:%S")

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
                if line.startswith("#","//"):
                    print(f"주석처리: {num}번째줄 : {line}")
            #이메일 탐지
            
    pre_file = cureent_file
    print("확인!!")
    time.sleep(1)