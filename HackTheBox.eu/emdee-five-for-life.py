# Based in https://gist.github.com/rarecoil/ code

import requests
import hashlib

URI = "http://docker.hackthebox.eu:43650"
PROXIES = {}  # {'http':'http://127.0.0.1:8080'}


def get_and_hash(ret):
    begin = ret.find("<h3 align='center'>") + 19
    end = ret.find("</h3>")
    md5_string = ret[begin:end].encode('utf-8')
    digest = hashlib.md5(md5_string).hexdigest()
    return digest


def get_flag_string(ret):
    begin = ret.find("<p align='center'>") + 18
    end = ret.find("</p>")
    string = ret[begin:end]
    return string

session = requests.Session()
req = session.get(URI, proxies=PROXIES)
md5 = get_and_hash(req.text)
print('\x1b[1;31mFor encode to MD5: \x1b[32m{0}\x1b[0m'.format(md5))
req = session.post(URI, data={"hash": md5}, proxies=PROXIES)
print(req.text)
string = get_flag_string(req.text)
print('\x1b[1;31mString Flag: \x1b[32m{0}\x1b[0m'.format(string))
