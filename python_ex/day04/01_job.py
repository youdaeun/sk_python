# 스케줄링 기본 샘플 코드
import schedule
import time

def job():
    print("Test입니다.")

schedule.every(3).seconds.do(job) # 3초마다 job 실행

while True:
    schedule.run_pending()
    time.sleep(1)