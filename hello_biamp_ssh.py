import paramiko
import time


def excute_command( cmd:str ) -> str :
    shell.send( cmd.encode(encoding='ascii') )
    time.sleep(1)
    return  shell.recv(128).decode(encoding='ascii')

HOST = "172.16.13.52"

# 创建SSH客户端对象

ssh = paramiko.SSHClient()


# 设置自动添加策略，允许连接未经验证的新主机（生产环境中应谨慎设置）

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


# 建立到远程服务器的SSH连接

ssh.connect(
    hostname= HOST,
    port=22,  # 默认SSH端口通常是22
    username="default",
    password=''
)

shell = ssh.invoke_shell()
time.sleep(1)
loginInfo = shell.recv(128).decode(encoding='ascii')
print(loginInfo)
time.sleep(1)
welcome = shell.recv(128).decode(encoding='ascii')
print(welcome)
sn_command = 'DEVICE get serialNumber\n'
get_mute_command = 'Level1 get mute 1\n'
sub_mute_command = 'Level1 subscribe mute 1 level_mute_sub 500 \n'
set_mute_command = 'Level1 set mute 1 false\n'

print("begin to fetch serialNumber")
response = excute_command( sn_command )
print(response)
time.sleep(1)
print("begin to fetch mute status")
response = excute_command( get_mute_command )
print(response)

response = excute_command(sub_mute_command)
print(response)

response = excute_command(set_mute_command)
print(response)

print("close ssh")
ssh.close()
