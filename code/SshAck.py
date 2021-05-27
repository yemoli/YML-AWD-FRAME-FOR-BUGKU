#!/usr/bin/env python3
import paramiko
import traceback
from loguru import logger
from config.SimpleConfig import *


class SSHLogin:
    def __init__(self,ip):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ip = ip
    def change_pwd(self, ip, port, login_user, modify_user, old_password, new_password):
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(hostname=ip, port=port, username=login_user, password=old_password, timeout=3)
            if login_user == "root":
                command = f"passwd {modify_user}\n"
                stdin, stdout, stderr = self.ssh.exec_command(command)
                stdin.write(new_password + '\n' + new_password + '\n')
            else:
                command = f"passwd \n"
                stdin, stdout, stderr = self.ssh.exec_command(command)
                stdin.write(old_password + '\n' + new_password + '\n' + new_password + '\n')
            out, err = stdout.read(), stderr.read()
            if "successfully" in str(out) or "successfully" in str(err):
                logger.success(f"{ip}:{port}密码修改成功")
            else:
                logger.error(f"{ip}:{port}密码修改失败{str(err)}")
            self.ssh.close()
        except paramiko.ssh_exception.AuthenticationException as e:
            logger.warning(f"{ip}:{port}账号密码错误{e}")
        except:
            # traceback.print_exc()
            logger.error(f"{ip}:{port}连接失败")

    def run(self,mod = "default"):
        ip = self.ip.strip()
        port = ip.split(":")[1]
        ip = ip.split(":")[0]
        if mod == "changepass":
            self.change_pwd(ip, port, login_user=LOGIN_USER, modify_user=MODIFY_USER,
                                old_password=OLD_PASSWORD,
                                new_password=NEW_PASSWORD)
        elif mod == "exec_cmd":
            self.ssh_exec_cmd(ip,port,login_user=LOGIN_USER,login_password=OLD_PASSWORD)
        else:
            return False
    def ssh_exec_cmd(self, ip, port, login_user, login_password):
        try:
            stderr = ""
            stdout = ""
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(hostname=ip, port=port, username=login_user, password=login_password, timeout=3)
            command = f"{CONFIG_SSH_CMD}"
            try:
                stdin, stdout, stderr = self.ssh.exec_command(command,timeout=3)
                # stdin.write(new_password + '\n' + new_password + '\n')
                result = stdout.read()
                logger.success(f"{ip}:{port}执行命令成功")
                return result
            except :
                logger.success(f"{ip}:{port}似乎执行命令成功")
        except paramiko.ssh_exception.AuthenticationException as e:
            logger.warning(f"{ip}:{port}账号密码错误{e}")
        except:
            # traceback.print_exc()
            logger.error(f"{ip}:{port}连接失败")
# SSHLogin().run()
#ip simple:10.0.0.1:2201
#更改ssh密码
def passh(ip='8.8.8.8:22'):
    SSHLogin(ip).run("changepass")

def ssh_cmd(ip='192.168.196.140:2201'):
    SSHLogin(ip).run("exec_cmd")

