#！/usr/bin/python3
#

import requests
import json
import sys
from  urllib import request

headers = {'Content-Type': 'application/json;charset=utf8'}     
api_url = 'https://oapi.dingtalk.com/robot/send?access_token=XXXXXXXX'   #  你的钉钉机器人地址
def msg(text):

    json_text = {
      "msgtype": "text",
        "at": {
            "atMobiles": [     # 需要@的人
                "15899526920"
            ],
            "isAtAll": False      # 是否需要@所有人
        },
        "text": {
            "content": text
        }
    }
    print(requests.post(api_url,json.dumps(json_text),headers=headers).content)


if __name__ == '__main__':
    text = sys.argv[1]
    msg(text)
