class data_link:
    def __init__(self,input_data):
        self.modified_data=input_data

class Encoder_data_link(data_link):
    encoded_frame={}
    def print_string(self):
        print(self.modified_data)
    
    def get_string(self):
        return self.modified_data
    
    def create_frame(self):
        self.encoded_frame["data"]=self.modified_data
        self.encoded_frame["ip_address"]="192.168.0.1"

    def get_frame(self):
        return self.encoded_frame

class Decoder_data_link(data_link):
    def print_string(self):
        print(self.modified_data)
    
    def get_string(self):
        return self.modified_data
