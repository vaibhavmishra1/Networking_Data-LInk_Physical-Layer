# program to receive data as a receiver 

import socket
import json
import pickle

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
PORT_DEST=65431
SOURCE="192.168.76.45"
DEST="192.168.1.5"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            try:
                dictio=pickle.loads(data)
            except EOFError:
                dictio={}
            if not data:
                break
            
            dest_ip=dictio["destination_ip_address"]
            if (dest_ip==SOURCE):
                print("target found")
                print("target ip address=",SOURCE)
                print(dictio)
            
            else:
                s.close()
                with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as t:
                    t.connect((HOST,PORT_DEST))
                    data_send=pickle.dumps(dictio)
                    t.sendall(data_send)



            