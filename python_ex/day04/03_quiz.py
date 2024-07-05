import os
import time
import re
from datetime import datetime
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Slack API 토큰과 메시지를 보낼 채널 설정
SLACK_API_TOKEN = "your_slack_api_token"
SLACK_CHANNEL ="your_slack_channel"

DIR_PATH = 'static'

def send_message(channel, text):
    client = WebClient(token=SLACK_API_TOKEN)

    try:
        # 채널에 메시지 전송
        response = client.chat_postMessage(
            channel=channel,
            text=text
        )
        # 응답 출력
        print("Message sent successfully:", response["message"]["text"])
    except SlackApiError as e:
        # 에러 처리
        print("Error sending message:", e.response["error"])   

pre_file = set(os.listdir(DIR_PATH))

while True:
    current_file = set(os.listdir(DIR_PATH))
    result_diff = current_file - pre_file

    for file_name in result_diff:
        if file_name.endswith(".php"):
            print(f"새로운 파일 탐지 : {file_name}")

            # 파일의 내용을 확인하기
            file_path = os.path.join(DIR_PATH, file_name)

            # Slack으로 메시지 전송
            send_message(SLACK_CHANNEL, f"Message sent successfully: Warning: A new .php file was uploaded to the directory!")
            send_message(SLACK_CHANNEL, f"File : {file_name}")
            send_message(SLACK_CHANNEL, f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} 파일 내용 {file_name}\n")

    pre_file = current_file
    print("확인!!")
    time.sleep(1)
