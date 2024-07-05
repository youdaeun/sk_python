import os
import time
import re
from datetime import datetime
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Slack API 토큰과 메시지를 보낼 채널 설정
SLACK_API_TOKEN = "your_slack_api_token"
SLACK_CHANNEL ="your_slack_channel"

# 파일 경로 설정
DIR_PATH = 'static'
FILE_NAME = 'example.php'
FILE_PATH = os.path.join(DIR_PATH, FILE_NAME)

# 파일 존재 여부 확인
if not os.path.exists(FILE_PATH):
    print(f"파일을 찾을 수 없습니다: {FILE_PATH}")
else:
    client = WebClient(token=SLACK_API_TOKEN)

    try:
        response = client.files_upload_v2(
            channel=SLACK_CHANNEL,
            file=FILE_PATH,
            initial_comment="Here is the document we discussed.",
            filename=FILE_NAME,
            title="테스트입니다"
        )
        print("파일 업로드 성공:", response["file"]["name"])
    except SlackApiError as e:
        print("파일 업로드 오류:", e.response["error"])
