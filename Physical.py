class physical:
    def __init__(self,input_frame):
        self.modified_frame=input_frame


class Encoder_physical(physical):
    def print_string(self):
        print(self.modified_frame)
    
    def get_string(self):
        return self.modified_frame

    def convert_AMI(self):
        inputs=self.modified_frame["data"]
        j=0
        ans=""
        for i in inputs:
            if i=='1':
                if j%2==0:
                    ans+='1'
                else:
                    ans+='-1'
                j+=1
            else:
                ans+='0'
        self.modified_frame["data"]=ans



class Decoder_physical(physical):
    def print_string(self):
        print(self.modified_frame)
    
    def get_string(self):
        return self.modified_frame