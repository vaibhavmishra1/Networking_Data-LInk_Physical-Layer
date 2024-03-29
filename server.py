# program to receive data as a receiver 

import socket
import json
import pickle
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

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
            print(dictio["data"])
            print(dictio["ip_address"])
            