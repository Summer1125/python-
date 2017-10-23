import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from urllib.request import  urlopen


def get(url):
    res = urlopen(url).read()
    print(res)

get('https://github.com/Summer1125/python_basics')

##爬网页的基本代码，可能会报关于SLL的证书错误，在代码最开始加上import ssl ssl=...就可解决

#下面是给爬网页一直send，send一次爬一次


import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from urllib.request import  urlopen


def get():
    while True:
        url = yield
        res = urlopen(url).read()
        print(res)

e = get()
next(e)
e.send('https://github.com/Summer1125/python_basics')



