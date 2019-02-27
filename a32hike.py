import json
import requests


def getactivitycomment(atid, page=1, pagesize=10):
    response = requests.post(
        'https://wx.32hike.com/wechat/v4/activity/getactivitycomment',
        headers={
            'Accept':
            'application/json, '
            'text/javascript, '
            '*/*; '
            'q=0.01',
            'Accept-Encoding':
            'gzip, '
            'deflate, '
            'br',
            'Accept-Language':
            'zh-CN,en-US;q=0.9',
            'Connection':
            'keep-alive',
            'Content-Type':
            'application/x-www-form-urlencoded; '
            'charset=UTF-8',
            'Cookie':
            'PHPSESSID=ifckvhjo6o9v7vlo8rlo047b52',
            'Origin':
            'https://wx.32hike.com',
            'Referer':
            'https://wx.32hike.com/wechat/activity/index/0/distance_2?aid=34377',
            'User-Agent':
            'Mozilla/5.0 '
            '(Linux; '
            'Android '
            '9; '
            'EML-AL00 '
            'Build/HUAWEIEML-AL00; '
            'wv) '
            'AppleWebKit/537.36 '
            '(KHTML, '
            'like '
            'Gecko) '
            'Version/4.0 '
            'Chrome/66.0.3359.126 '
            'MQQBrowser/6.2 '
            'TBS/044504 '
            'Mobile '
            'Safari/537.36 '
            'MMWEBID/3844 '
            'MicroMessenger/7.0.3.1400(0x2700033A) '
            'Process/tools '
            'NetType/WIFI '
            'Language/zh_CN',
            'X-Requested-With':
            'XMLHttpRequest'
        },
        data={'atid': atid, 'page':page,'pagesize': pagesize})

    return response.json()

if __name__ == '__main__':
    print(json.dumps(getactivitycomment(81, page=1)))
