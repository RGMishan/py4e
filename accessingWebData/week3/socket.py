import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #connection with interenet without linking
mysock.connect( ('data.pr4e.org', 80) ) #data.pr4e.org is host and 80 is port