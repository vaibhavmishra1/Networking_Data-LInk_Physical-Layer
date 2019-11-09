class data_link:
    def __init__(self,input_data):
        modified_data=self.binary_conversion(input_data)
        self.modified_data=modified_data
    
    def binary_conversion(self,s):
        result = []
        for c in s:
            bits = bin(ord(c))[2:]
            bits = '00000000'[len(bits):] + bits
            result.extend([int(b) for b in bits])
        result_str=""
        for r in result:
            if r==0:
                result_str+="0"
            else:
                result_str+="1"
        
        return result_str
    
    def binary_decoder(self,bits_str):
        chars = []
        bits=[]
        for b in bits_str:
            bits.append(b)
        for b in range(len(bits) //8):
            byte = bits[b*8:(b+1)*8]
            chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
        result_str=""
        for r in chars:
            result_str+=r
        return result_str

class Encoder_data_link(data_link):
    encoded_frame={}
    def __init__(self,input_data):
        data_link.__init__(self,input_data)
        self.create_frame()

    def print_string(self):
        print_data=data_link.binary_decoder(data_link,self.modified_data)
        print(print_data)
    
    def get_string(self):
        return self.modified_data
    
    def create_frame(self):
        self.encoded_frame["data"]=self.modified_data
        self.encoded_frame["ip_address"]="192.168.0.1"
        
    
    def cycle_redundancy_check(self,key):
        self.encoded_frame["key"]="key"
        print("crc...")





    def get_frame(self):
        return self.encoded_frame

class Decoder_data_link(data_link):
    def print_string(self):
        print(self.modified_data)
    
    def get_string(self):
        return self.modified_data
