# program to send data from sender


import socket
import Data_Link
import Physical
import json
import pickle
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
send_data="sending data from sender to receiver"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data_link_encoder=Data_Link.Encoder_data_link(send_data)
    data_link_encoder.create_frame()
    passed_data_link=data_link_encoder.get_frame()
    print(passed_data_link["data"])
    print(passed_data_link["ip_address"])


    physical_class=Physical.physical(passed_data_link)
    passed_physical=physical_class.modified_data


    data= pickle.dumps(passed_physical) #data serialized
    s.sendall(data)

