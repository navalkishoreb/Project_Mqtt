#!/usr/bin/python

import socket

s= socket.socket();
host = socket.gethostname();
port = 12345;
s.bind((host,port));

s.listen(5);

while(True):
	c, addr = s.accept();
	print 'got connection form',addr;
	c.send('thank you for connecting');
	while True:
		buffer =c.recv(4096);
		print buffer;	
