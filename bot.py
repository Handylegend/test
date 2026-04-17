import os
import requests

# 从环境变量中读取 URL
WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')

def send_message():
    data = {
        "content": "🚀 你好！这是一条来自 GitHub Actions 的定时自动消息。",
        "username": "极简推送助手"
    }
    
    response = requests.post(WEBHOOK_URL, json=data)
    
    if response.status_code == 204:
        print("消息发送成功！")
    else:
        print(f"发送失败，状态码: {response.status_code}")

if __name__ == "__main__":
    send_message()
