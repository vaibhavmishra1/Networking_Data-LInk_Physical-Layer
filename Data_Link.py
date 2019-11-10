def xor(a, b):
        result = [] 
        # Traverse all bits, if bits are 
        # same, then XOR is 0, else 1 
        for i in range(1, len(b)): 
            if a[i] == b[i]: 
                result.append('0') 
            else: 
                result.append('1') 
    
        return ''.join(result) 



def mod2div(divident,divisor):
        pick = len(divisor)
        tmp = divident[0 : pick] 
        while pick < len(divident): 
            if tmp[0] == '1':
                tmp = xor(divisor, tmp) + divident[pick] 
    
            else:
                tmp = xor('0'*pick, tmp) + divident[pick] 
            pick += 1
        if tmp[0] == '1': 
            tmp = xor(divisor, tmp) 
        else: 
            tmp = xor('0'*pick, tmp) 
    
        checkword = tmp 
        return checkword 



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
    
    def encodeData(self,data, key): 
        l_key = len(key) 
        # Appends n-1 zeroes at end of data 
        appended_data = data + '0'*(l_key-1) 
        remainder = mod2div(appended_data,key) 

        # Append remainder in the original data 
        codeword = data + remainder 
        print("Remainder : ", remainder) 
        print("Encoded Data (Data + Remainder) : ", 
            codeword) 
        self.modified_data=codeword

class Encoder_data_link(data_link):
    encoded_frame={}
    def __init__(self,input_data,SOURCE_IP_ADDR,DEST_IP_ADDR,PORT):
        data_link.__init__(self,input_data)
        self.create_frame(SOURCE_IP_ADDR,DEST_IP_ADDR,PORT)

    def print_string(self):
        print_data=data_link.binary_decoder(data_link,self.modified_data)
        print(print_data)
    
    def get_string(self):
        return self.modified_data
    
    def create_frame(self,SOURCE_IP_ADDR,DEST_IP_ADDR,PORT):
        self.encoded_frame["data"]=self.modified_data
        self.encoded_frame["source_ip_address"]=SOURCE_IP_ADDR
        self.encoded_frame["destination_ip_address"]=DEST_IP_ADDR
        self.encoded_frame["physical_address"]=PORT

    def cycle_redundancy_check(self,key):
        self.encoded_frame["key"]=key
        print("crc...")
        data_link.encodeData(data_link,self.modified_data,key)
        self.encoded_frame["data"]=self.modified_data
    

    def get_frame(self):
        return self.encoded_frame

class Decoder_data_link(data_link):
    def print_string(self):
        print(self.modified_data)
    
    def get_string(self):
        return self.modified_data
