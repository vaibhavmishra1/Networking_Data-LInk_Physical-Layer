# program to send data from sender


import socket
from Data_Link import Encoder_data_link 
import Physical
import json
import pickle
SOURCE='192.168.0.3'
DEST="192.168.1.5"
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
send_data="socket programming"
send_data=str(input())
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data_link_encoder=Encoder_data_link(send_data,SOURCE,DEST,PORT)
    data_link_encoder.print_string()
    data_link_encoder.cycle_redundancy_check(key="100101")
    print("do you want to induce error: type 1 or 0")
    inp=int(input())
    if inp==1:
        data_link_encoder.induce_error(error="1010")
    data_link_encoder.print_string()
    passed_data_link=data_link_encoder.get_frame()
    
    physical_class=Physical.Encoder_physical(passed_data_link)
    physical_class.convert_AMI()
    passed_physical=physical_class.modified_frame
    print(passed_physical)

    data= pickle.dumps(passed_physical) #data serialized
    s.sendall(data)

