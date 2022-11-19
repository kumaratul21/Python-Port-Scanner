#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setimeout(5)
#ip of vulnerable website ex 123.23.123.1233
host = input('please enter ip you want to scan ")

#PORT YOU WANT TO CHECK
port = int(input('please enter the port u want to scan"))

  

def portscanner(port):
	#RETURNS ERROR CODE OR RAISE EXCEPTION WHEN ERROR OCCURS
	If s.connect_ex((host, port)):
		Print("the port is closed")
	Else:
		Print("the port is open")

#CALLING PORT SCANNER
portscanner(port)