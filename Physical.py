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
        print("inputs=",self.modified_frame["data"])
        j=0
        ans=""
        for i in inputs:
            if i=='1':
                if j%2==0:
                    ans+='1'
                else:
                    ans+="-1"
                j+=1
            else:
                ans+='0'
        self.modified_frame["data"]=ans



class Decoder_physical(physical):
    def __init__(self,modified_frame):
        physical.__init__(physical,modified_frame)

    def print_frame(self):
        print(self.modified_frame)
    
    def get_frame(self):
        return self.modified_frame

    def convert_AMI(self):
        inputs=self.modified_frame["data"]
        i=0
        ans=""
        while(i<len(inputs)):
            if inputs[i]=='-':
                i+=1
                ans+='1'
            elif inputs[i]=='1':
                ans+='1'
            else:
                ans+='0'
            i+=1
        self.modified_frame["data"]=ans
    
    