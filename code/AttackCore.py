#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import hashlib
import base64
from loguru import logger
import threading
import time
import hmac
import gzip
from db.Utils import *
from code.SshAck import *
from code.BehinderAck import *
# 常见加解密类
class Utils:
    def __init__(self):
        pass

    @staticmethod
    def md5_encode(strings):
        hash = hashlib.md5()
        hash.update(strings.encode('utf-8'))
        md5_sign = hash.hexdigest()
        return md5_sign

    @staticmethod
    def sha1_encode(strings):
        hash = hashlib.sha1()
        hash.update(strings.encode('utf-8'))
        sha1_sign = hash.hexdigest()
        return sha1_sign

    @staticmethod
    def sha256_encode(strings):
        hash = hashlib.sha256()
        hash.update(strings.encode('utf-8'))
        sha256_sign = hash.hexdigest()
        return sha256_sign

    @staticmethod
    def hmac_sha256(strings, key):
        return hmac.new(key.encode(), strings.encode(), digestmod=hashlib.sha256).hexdigest()

    @staticmethod
    def hmac_sha1(strings, key):
        return hmac.new(key.encode(), strings.encode(), digestmod=hashlib.sha1).hexdigest()

    @staticmethod
    def b64dec(strings):
        return base64.b64decode(str(strings))

    @staticmethod
    def b64enc(strings):
        return base64.b64encode(strings.encode())

    @staticmethod
    def b32dec(strings):
        return base64.b32decode(str(strings))

    @staticmethod
    def b32enc(strings):
        return base64.b32encode(strings.encode())

    @staticmethod
    def b16dec(strings):
        return base64.b16decode(str(strings))

    @staticmethod
    def b16enc(strings):
        return base64.b16encode(strings.encode())

    @staticmethod
    def gzip_decompress(strings):
        return gzip.decompress(strings.encode())

    @staticmethod
    def gzip_compress(strings):
        return gzip.compress(strings.encode())


# 覆盖requests.session的类
class Session:
    def __init__(self):
        self.ses = requests.session()

    def post(self, url, data=None, json=None, **kwargs):
        try:
            return self.ses.post(url, data=data, json=json, timeout=10, **kwargs)
        except BaseException as e:
            pass
            # logger.error(f"[{url}]请求失败")#，原因:{e}

    def get(self, url, **kwargs):
        try:
            return self.ses.get(url, timeout=10, **kwargs)
        except BaseException as e:
            pass
            # logger.error(f"[{url}]请求失败")#，原因:{e}

    def put(self, url, **kwargs):
        try:
            return self.ses.put(url, timeout=10, **kwargs)
        except BaseException as e:
            pass
            # logger.error(f"[{url}]请求失败")#，原因:{e}


# 多线程攻击类
class Attack:
    #mod:减少不必要的查询模块
    def __init__(self,mod="init"):
        self.ips = []
        self.ip_flag = []
        self.shells = []
        self.ssh_config = []
        self.behinders = []
        self.softLinks = []
        if mod == "ssh":
            self.__get_ssh_config()
        if mod == "behinder":
            self.__get_behinders()
        if mod == "softlink":
            self.__get_solflink()
        self.__get_ips()
        self.__get_ip_flag()
        self.__get_shells()

    def __get_behinders(self):
        result = select_behinder()
        for row in result:
            self.behinders.append(row)
    def __get_shells(self):
        result = select_shell()
        for row in result:
            self.shells.append(row)

    def __get_ips(self):
        result = select_ip()
        for row in result:
            self.ips.append(row[0])
    def __get_ip_flag(self):
        result = select_flag()
        for row in result:
            self.ip_flag.append(row)
    def __get_ssh_config(self):
        result = select_ssh()
        for row in result:
            self.ssh_config.append(row[0])
    def __get_solflink(self):
        result = select_softLink()
        for row in result:
            self.softLinks.append(row)
    @staticmethod
    def __generate_flag_json(ip, flag):
        json = {
            "ip": ip,
            "flag": flag,
            "time": int(time.time() * 1000)
        }
        return json

    #批量获取flag多线程函数
    def attack(self, func):
        # print(self.ips)
        logger.debug(self.ips)
        for i in range(0, len(self.ips)):
            try:
                # logger.info(f'当前攻击进度{i}/{len(self.ips)}，攻击ip为{self.ips[i]}')
                t = threading.Thread(target=func, args=(self.ips[i],))
                t.start()
            except BaseException:
                pass
    def trans_flag(self, func):
        # print(self.ips)
        thread_list = []
        logger.debug(self.ip_flag)
        for i in range(0, len(self.ip_flag)):
            try:
                # print(self.ip_flag[i][1])
                # logger.info(f'当前攻击进度{i}/{len(self.ips)}，攻击ip为{self.ips[i]}')
                t = threading.Thread(target=func, args=(self.ip_flag[i][0],self.ip_flag[i][1]))
                thread_list.append(t)
                t.start()
            except BaseException:
                pass
        for ts in thread_list:
            ts.join()
    def ack_memshell(self,func):
        logger.debug(self.shells)
        thread_list = []
        for i in range(0, len(self.shells)):
            try:
                # print(self.ip_flag[i][1])
                # logger.info(f'当前攻击进度{i}/{len(self.ips)}，攻击ip为{self.ips[i]}')
                #参数 webshell,pass,method
                t = threading.Thread(target=func, args=(self.shells[i][1],self.shells[i][2],self.shells[i][3]))
                thread_list.append(t)
                t.start()
            except BaseException:
                pass
        for ts in thread_list:
            ts.join()
    #更改ssh密码,执行命令函数
    def ack_ssh(self,func):
        thread_list = []
        for i in range(0,len(self.ssh_config)):
            try:
                # print(self.ssh_config[i])
                t = threading.Thread(target=func, args=(self.ssh_config[i],))
                thread_list.append(t)
                t.start()
            except BaseException:
                pass
        for ts in thread_list:
            ts.join()

    def ack_behinder(self,func):
        thread_list = []
        for i in range(0,len(self.behinders)):
            try:
                t = threading.Thread(target=func, args=(self.behinders[i][1],self.behinders[i][2],))
                thread_list.append(t)
                t.start()
            except:
                pass
        for ts in thread_list:
            ts.join()
    def ack_softLink(self,func):
        thread_list = []
        for i in range(0, len(self.softLinks)):
            try:
                t = threading.Thread(target=func, args=(self.softLinks[i][1], self.softLinks[i][2],))
                thread_list.append(t)
                t.start()
            except:
                pass
        for ts in thread_list:
            ts.join()
##发送攻击请求


Attack("softlink")



