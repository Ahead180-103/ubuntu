#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: aiker@gdedu.ml
# My blog http://m51cto.51cto.blog.com 
import requests
import json
import sys
import os
 
headers = {'Content-Type': 'application/json;charset=utf-8'}
api_url = "https://oapi.dingtalk.com/robot/send?access_token=******"
 
def msg(text):
    json_text= {
     "msgtype": "text",
        "at": {
            "atMobiles": [
                "177******76"
            ],
            "isAtAll": False
        },
        "text": {
            "content": text
        }
    }
    print(requests.post(api_url,json.dumps(json_text),headers=headers).content)
     
if __name__ == '__main__':
    text = sys.argv[1]
    msg(text)
