# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def login():
    header = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch, br',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cache-Control':'max-age=0',
        'Connection': 'keep-alive',
        'User-Agent':  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110'
    }
    session = requests.session()
    res = session.get('http://www.zhihu.com',headers = header).content
    _xsrf = BeautifulSoup(res, "html.parser").find('input', attrs={'name': '_xsrf'})['value']

    login_data = {
        '_xsrf':_xsrf,
        'password':'3926839',
       # 'remember_me':'true',
        'phone_num':'18827553215',
        'captcha_type': 'cn'

    }
    session.post('https://www.zhihu.com/login/phone_num',data = login_data,headers = header)
    res = session.get('http://www.zhihu.com')
    print(res.text)

if __name__ == '__main__':
    login()