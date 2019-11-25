#################DATA COMMUNICATION PROJECT ##########################################

BY- Vaibhav Mishra  (B17CS057)                                     Instructor- Prof. Sumit Kalra
    Muzzafer Ali    (B17CS037)


            --Implementation of concepts of Data-Link Layer and Physical Layer in Networking--


Code Modules---
                1-Data_Link.py- Consists of Data Link Class consisting of functionalities for implementing 
                                Data-Link Layer features.
                                Consist of Data_Link parent class and two inherited child class namely 
                                Encoder_Data_Link and Decoder_Data_Link.
                                Encoder Data Link class object is formed by the sender and Decoder_Data_Link 
                                class object is formed by the receiver. the intermediate nodes consists of both
                                Enocding and Decoding the data hence both classes are used.

                2-Physical.py-  Consists of Physical Class consisting of functionalities for implementing 
                                Physical Layer features.
                                Consist of Physical parent class and two inherited child class namely 
                                Encoder_Physical and Decoder_Physical.
                                Encoder Physical class object is formed by the sender and Decoder_Physical 
                                class object is formed by the receiver. the intermediate nodes consists of both
                                Enocding and Decoding the data hence both classes are used.
                
                3-client.py-    Client.py is the module for sending the information through the networking 
                                and actually encoding the data through physical and data link layer.
                                it has an address and sends a message to the the destination address.
                
                4-server2.py-   It is an intermidiate node. It first decodes the data and checks if it is the 
                                destination, if not it encodes the data again and passes the data to next node.
                                hence, both encoding and decoding takes place in this node.

                5-server3.py-   It is an intermidiate node. It first decodes the data and checks if it is the 
                                destination, if not it encodes the data again and passes the data to next node.
                                hence, both encoding and decoding takes place in this node.
                            
                6-server.py-    Server.py is the destination node for receiving the information.
                                it decodes the data and checks for destination address and after it matches with 
                                its address. it performs decryption and error checking.


Data Link Layer-
various algorithm used in data link layer are- 
    1-Error detection using Cycle redundancy check
    2-Bit Stuffing
    3-encaptulation and decaptulation from frame
    4-address matching
    5-induce error

Physical Layer-
various algorithm used in Physical layer is-:
    1-conversion to binary information and vice versa
    2-conversion to AMI and vice versa


