# Abitha-M
# modules used
import socket

hostname = socket.gethostname()
client_address_family = socket.AF_INET
client_protocol = socket.SOCK_STREAM
client_skt = socket.socket(client_address_family, client_protocol)
IPAddr = socket.gethostbyname(hostname)
client_ip = socket.gethostbyname(IPAddr) # gets the ip address of the hosting system
print(IPAddr)
client_port = 9001
server_port = 9008
server_ip = "192.168.29.138"
client_skt.bind((client_ip, client_port))

# connecting to server
client_skt.connect((server_ip, server_port))

client_skt.recv(1024)

while True:
    command = input()
    id="1221"   

    if command.strip() == "":
        print("Empty command")
    else:
        client_skt.send(command.strip().encode())
        response = client_skt.recv(1024)
	client_skt.send(id.strip().encode())
    	id = client_skt.recv(1024)
        print(response, "ID:", id, "\n")
    if command.strip() == "exit()":
        break
