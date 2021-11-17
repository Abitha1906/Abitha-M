# importing required libraries
import socket
import threading
import datetime
import sys, subprocess

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print(IPAddr)

#creates and returns a socket
def create_socket():
    #Protocol = UDB, addressFamily = ipv4
    protocol = socket.SOCK_STREAM
    address_family = socket.AF_INET
#socket creation
    skt = socket.socket(address_family, protocol)
#Bind information
    server_ip = ""
    server_port = 9008
#Binding port and ip
    skt.bind((server_ip, server_port))
    return skt
skt = create_socket()

# listening for incomming connection requests from clients
skt.listen()

# processing requests
def request_processor(skt_object, address_info):
    # constandly listens for data from client
    while True:
        request = skt_object.recv(1024)
        
        # checks whether user wants to terminate session
        if request.decode('utf-8') == "exit()":
            skt_object.send(b"Session terminated")
            skt_object.close()
            break
            
        # executes requests and returns output
        status_output = subprocess.getstatusoutput(request)
        
        # returns output to user
        skt_object.send(status_output[1].encode())
        
        # logs request
        logger({"request": request, "address_info": address_info, "datetime"
