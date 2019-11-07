# program to send data from sender


import socket
import Data_Link
import Physical
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
send_data="sending data from sender to receiver"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data_link_class=Data_Link.data_link(send_data)
    passed_data_link=data_link_class.modified_data


    physical_class=Physical.physical(passed_data_link)
    passed_physical=physical_class.modified_data

    my_str_as_bytes = str.encode(passed_physical)
    s.sendall(my_str_as_bytes)

