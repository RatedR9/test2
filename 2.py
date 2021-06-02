from multiprocessing import  *
import requests
import os
import json

def sign(e,p):
    url = 'https://v2.bujidao.org/auth/login'
    headers = {
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15'
    }
    data = {
        'email': ''+e,
        'passwd': ''+p,
        'code': ''
    }
    res = requests.post(url=url,headers=headers,data=data)
    print(res.cookies)
    return res.cookies['uid'],res.cookies['email'],res.cookies['key'],res.cookies['ip'],res.cookies['expire_in']
def parse():
    u=sign()
    for i in range(len(u)):
        uid = u[0]
        email = u[1]
        key = u[2]
        ip = u[3]
        expire_in = u[4]
    c='uid={};email={};key={};ip={};expire_in={}'.format(uid,email,key,ip,expire_in)

    return c






def main():
    url = 'https://v2.bujidao.org/user/checkin'
    c=parse()

    print(c)

    headers = {
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15',
        'Cookie':''+c
    }
    res = requests.post(url=url,headers=headers)

    x = [os.environ['EMAIL1'],os.environ['EMAIL2']]
    y = [os.environ['PASSWD1'],os.environ['PASSWD2']]
    args = list(zip(x, y))
    with Pool(5) as p:
        p.starmap_async(sign,args).wait()
    print(res.text)


if __name__ == '__main__':
    main()
