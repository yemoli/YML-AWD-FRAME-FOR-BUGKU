from code.AttackCore import *
import re
from db.Utils import *
session = Session()
utils = Utils()
threadLock = threading.Lock()

def reqFlagServer(ip,flag):
    ##如果需要录入对应ip的flag，靶机为一个ip，请去掉下面的这行注释
    #ip = ip.split(":")[0]
    ###Don't use (import request)
    #############################################################
    burp0_url = "https://ctf.bugku.com:443/awd/submit.html"
    burp0_cookies = {"__yjs_duid": "1_3bd90111a9b249458bb95221633ddce91610886261713", "think_lang": "zh-cn",
                     "PHPSESSID": "0d7b2838faf899f2036f5184921019ac",
                     "autoLogin": "xI0OuIIXi382hQQsxG98rnS9Z0dSe7yDR6%2BGSgXExdEeErYLlG0WVSjSEcn982AjsUS8unH6MfzCyJ5VML%2Fb2r1iTAccEn%2FzBQRICvBwlV8dLGtyostKzhnrehTe%2BwvkSkpieb5Z1Ss",
                     "X-CSRF-TOKEN": "3da11de9c456c8b4b1df857ab528b300",
                     "__cfduid": "d175eb091919444086a8681ee544be6fb1610886308",
                     "Hm_lvt_97426e6b69219bfb34f8a3a1058dc596": "1610886308",
                     "Hm_lpvt_97426e6b69219bfb34f8a3a1058dc596": "1610886480"}
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0",
                     "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                     "Accept-Encoding": "gzip, deflate, br",
                     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                     "X-CSRF-TOKEN": "3da11de9c456c8b4b1df857ab528b300", "X-Requested-With": "XMLHttpRequest",
                     "Origin": "https://ctf.bugku.com", "Connection": "keep-alive",
                     "Referer": "https://ctf.bugku.com/awd/match/id/10.html"}
    burp0_data = {"flag": f"{flag}", "id": "39", "token": "c5de68e7bfd163eba5db0b9efa04db0f"}
    res = session.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data, verify=False)
    # print(res.text)
    # print(res.text)
    ############################################################
    try:
        logger.info(f"[+]{ip}  "+res.text)
    except:
        logger.info(f"[-]{ip}")
