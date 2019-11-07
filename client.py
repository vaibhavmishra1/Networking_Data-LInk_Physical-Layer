# program to send data from sender


import socket
import Data_Link
import Physical
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
send_data="sending data from sender to receiver"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    passed_data_link=Data_Link.data_link(send_data)
    passed_physical=Physical.physical(passed_data_link)
    s.sendall(send_data)

