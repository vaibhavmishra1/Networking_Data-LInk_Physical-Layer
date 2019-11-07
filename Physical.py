class physical:
    def __init__(self,input_data):
        self.modified_data=input_data


class Encoder_physical(physical):
    def print_string(self):
        print(self.modified_data)
    
    def get_string(self):
        return self.modified_data


class Decoder_physical(physical):
    def print_string(self):
        print(self.modified_data)
    
    def get_string(self):
        return self.modified_data