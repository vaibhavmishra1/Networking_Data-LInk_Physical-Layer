# program to receive data as a receiver 

import socket
import json
import pickle
from Data_Link import Decoder_data_link
from Physical import Decoder_physical
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65431     # Port to listen on (non-privileged ports are > 1023)
PORT_DEST=65430
SOURCE="192.168.1.5"
DEST="192.168.6.8"
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
            
            dest_ip=dictio["destination_address"]
            if (dest_ip==SOURCE):
                print("target found")
                print("target ip address=",SOURCE)
                decoder_class=Decoder_physical(dictio)
                decoder_class.convert_AMI()
                print(decoder_class.get_frame())
                decoder_data_link_class=Decoder_data_link(dictio)
                decoder_data_link_class.cycle_redundancy_check()
                decoder_data_link_class.extract_input()
            else:
                s.close()
                print("current address=",SOURCE)
                print("forwarding request to address=",DEST)
                with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as t:
                    t.connect((HOST,PORT_DEST))
                    data_send=pickle.dumps(dictio)
                    t.sendall(data_send)
                    t.close()



            