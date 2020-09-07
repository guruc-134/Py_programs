import socket
mysoc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysoc.connect(('coursera.org',80))
cmd='GET https://www.coursera.org/learn/python-network-data/home/welcome HTTP/1.0\r\n\r\n'.encode()
mysoc.send(cmd)

while True:
    data=mysoc.recv(512)
    if len(data)<1:
        break
    print(data.decode(),end='')
mysoc.close()
