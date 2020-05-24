import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connection with interenet without linking just a doorway
mysock.connect( ('data.pr4e.org', 80) ) 
#data.pr4e.org is host and 80 is port and we try connecting
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
#server does receive first and client do send first 
# the above code is preparing to send the request
mysock.send(cmd) # sending the above request

while True:
 data = mysock.recv(512)
 if (len(data) < 1):
  break
 print(data.decode(),end='')

mysock.close()

'''
My Program Consists
-socket
-connect
-send
-receive
Socket create a doorway and connect through port 80

then access the web pages of allocated website
'''