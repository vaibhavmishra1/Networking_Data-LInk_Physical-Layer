# program to send data from sender


import socket
from Data_Link import Encoder_data_link 
import Physical
import json
import pickle
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
send_data="sending data from sender to receiver"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data_link_encoder=Encoder_data_link(send_data)
    data_link_encoder.cycle_redundancy_check(key="1001")
    data_link_encoder.print_string()
    passed_data_link=data_link_encoder.get_frame()
    

    physical_class=Physical.physical(passed_data_link)
    passed_physical=physical_class.modified_data


    data= pickle.dumps(passed_physical) #data serialized
    s.sendall(data)

