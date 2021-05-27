# coding=utf-8
from db.Utils import *
import time
from tqdm import tqdm
from config.SimpleConfig import *

#获取ip列表(demo: 192.168.0.1-99)
#return list
def get_ip_list(x):
    ipList = []
    iplist = x.split('.')
    if '-' in x:
        for i in iplist:
            d = i
            if '-' in d:
                p = iplist.index(d)
                l = d.split('-')
                m = int(l[0])
                n = int(l[1])
        for j in range(m,n + 1):
            iplist[p] = str(j)
            ip = '-'.join(iplist)
            ipList.append(ip)
        ipList = sorted(set(ipList),key = ipList.index)
    else:
        ip = '-'.join(iplist)
        ipList.append(ip)
        ipList = sorted(set(ipList),key = ipList.index)
    return ipList

#获取端口列表(demo: 8801-8080)
#return list
def get_port_list(port):
    port_list = []
    if '-' in port:
        plist = port.split('-')
        m = int(plist[0])
        n = int(plist[1])
        for i in range(m, n + 1,portep):
            i = str(i)
            port_list.append(i)
    else:
        port_list.append(port)
    return port_list

def save_address(ip_list=[],port_list=[]):
    strip = ""
    for ip in ip_list:
        for port in port_list:
            strip = strip+"('"+ip+".awd.bugku.cn:"+port+"'),"
    sql = """insert into ipList (ip)values"""+strip[:-1]+";"
    try:
        execute_sql(sql)
        return True
    except:
        return False

def remove_address(ip_list=[],port_list=[]):
    strip=""
    for ip in ip_list:
        for port in port_list:
            strip = ip+":"+port
            try:
                sql = """DELETE FROM ipList WHERE ip = '"""+strip+"""';"""
                execute_sql(sql)
            except:
                print("[-]"+strip)
def remove_ssh(ip_list=[],port_list=[]):
    strip = ""
    for ip in ip_list:
        for port in port_list:
            strip = ip + ":" + port
            try:
                sql = """DELETE FROM sshIp WHERE ip = '""" + strip + """';"""
                execute_sql(sql)
            except:
                print("[-]" + strip)

def yml_init():
    sql = "Delete from ipList;"
    try:
        execute_sql(sql)
        return True
    except:
        return False


def progress_test(num=20):
    for i in tqdm(range(num)):
        time.sleep(1)
  # bar_length=20
  # for percent in range(0, 21):
  #   hashes = '#' * int(percent/20.0 * bar_length)
  #   spaces = ' ' * (bar_length - len(hashes))
  #   sys.stdout.write("\rNext Attack: [%s] %d%%"%(hashes + spaces, percent))
  #   sys.stdout.flush()
  #   time.sleep(1)


#保存ssh IP信息
def save_ssh(ip_list=[],port_list=[]):
    strip = ""
    for ip in ip_list:
        for port in port_list:
            strip = strip + "('" + ip + ":" + port + "'),"
    sql = """insert into sshIp (ip)values""" + strip[:-1] + ";"
    try:
        execute_sql(sql)
        return True
    except:
        return False


def softLinkRand():
    import random
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    characters = random.sample(alphabet, 2)
    rand = ''.join(characters)
    return rand
# softLinkRand()
