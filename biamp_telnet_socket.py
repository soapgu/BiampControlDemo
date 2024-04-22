import socket
import time

def negotiation():
    time.sleep(1)
    echo = connect.recv(128)
    print(echo.hex())
    # ff fc 18 ff fc 20 ff fc 23 ff fc 27 ff fc 24
    connect.sendall(bytes([0xff, 0xfc, 0x18,0xff,0xfc,0x20,0xff,0xfc,0x23,0xff,0xfc,0x27,0xff,0xfc,0x24]))
    time.sleep(1)
    echo = connect.recv(128)
    print(echo.hex())
    # ff fe 03 ff fc 01 ff fc 22 ff fc 1f ff fe 05 ff fc 21
    connect.sendall(bytes([0xff, 0xfe, 0x03,0xff,0xfc,0x01,0xff,0xfc,0x22,0xff,0xfc,0x1f,0xff,0xfc,0x05,0xff,0xfc,0x21]))
    time.sleep(1)
    welcome = connect.recv(128)
    print(welcome)

def send_cmd( cmd:str ):
    request_raw = f'{cmd}\n'.encode('ascii')
    connect.sendall( request_raw )
    time.sleep(1)
    data = connect.recv(128)
    print(data.decode('ascii'))

connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address =('172.16.13.52' , 23)
connect.setblocking(True)
connect.connect(server_address)
negotiation()
send_cmd('DEVICE get serialNumber\n')
send_cmd('Level1 get mute 1\n')
connect.close()



