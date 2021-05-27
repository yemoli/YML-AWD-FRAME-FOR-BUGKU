from code.CmdColor import *
import requests
from code.RecvCmd import *
from config.SendReq import *
from config.ReqFlagServer import *
threadLock = threading.Lock()
def auto_reqgetflag():
    try:
        init_flag()
        f = open('flag.txt', 'w+', encoding='utf8')
        f.write("")
        f.close()
        attack = Attack()
        attack.attack(func=payload)
        time.sleep(2)
    except:
        printRed("[-]执行过程遇到错误，错误代码:1003")


def auto_submitflag():
    try:
        attack = Attack()
        attack.trans_flag(func=reqFlagServer)
        time.sleep(2)
    except:
        printRed("[-]执行过程遇到错误，错误代码:1004")

def auto_recvgetflag():
    try:
        init_flag()
        f = open('flag.txt', 'w+', encoding='utf8')
        f.write("")
        f.close()
        try:
            ip_flag = auto_exec_recvcmd()
            # flag = re.findall(r"([a-fA-F\d]{32})", flag)
            # flag = re.findall(r"([a-fA-F\d]{32})", res.text) 匹配32位字符串
            # flag = re.findall(r"flag\{.*\}",res.text) 匹配花括号
            for ip in ip_flag:
                flag = ip_flag[ip].strip()
                print(ip+"->"+flag)
                insert_flag(ip=ip,flag=flag)
                write_flag(flag)
        except:
            pass
    except:
        printRed("[-]执行过程遇到错误，错误代码:1016")
def auto_solkflag(ip,softLink):
    try:
        html = requests.get(softLink,timeout=3)
        try:
            flag = html.text.strip()
            printGreen(f"[+]{softLink}->{flag}")
            threadLock.acquire()
            insert_flag(ip, flag)
            write_flag_text(flag)
            threadLock.release()
        except:
            pass
    except:
        printRed(f"[-]{softLink}")
