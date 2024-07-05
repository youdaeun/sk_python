import requests

slack_url = "your_slack_url"

def sendSlackWebHook(strText):
    headers = {
        "Content-type": "application/json"
    }
    
    data = {
        "text": strText
    }
    res = requests.post(slack_url, headers=headers, json=data)

# curl -X POST -H 'Content-type: application/json' --data '{"text":"Hello, World!"}' https://hooks.slack.com/services/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

    if res.status_code == 200:
        return "OK"
    else:
        return "Error"

print(sendSlackWebHook("파이썬 자동화 슬랙 메시지 테스트"))