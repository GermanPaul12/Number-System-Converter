from unittest import result


class Zahlensysteme:
    def __init__(self):
        pass
        
        
    def binary_to_decimal(self, num):
        return int(num, base=2)           
    
    
    def decimal_to_binary(self,num):  
        return bin(int(num)).replace("0b", "")
    
    
    def octal_to_binary(self,octnum): 
        return bin(int(octnum, base=8)).replace("0b", "")
    
    
    def binary_to_octal(self, num):
        return oct(int(num, base=2)).replace("0o", "")
        
   
    def hex_to_decimal(self,num):
        return int(num, base=16)    
    
    
    def decimal_to_hex(self, num):
        return str(hex(int(num)))[2:]
    
    
    def hex_to_binary(self,num):
        result = self.hex_to_decimal(num)
        return self.decimal_to_binary(result)


    def binary_to_hex(self, num):
        num = self.binary_to_decimal(num)
        return self.decimal_to_hex(num)    
    
    
    def octal_to_hexa(self, num): 
        result = self.octal_to_binary(num)
        return self.binary_to_hex(result)
    
    
    def hex_to_octal(self, num):
        result = self.hex_to_binary(num) 
        return self.binary_to_octal(result)   

    
    def decimal_to_octal(self, num):
        result = self.decimal_to_binary(num)
        return self.binary_to_octal(result).replace("0o", "")
    
    
    def octal_to_decimal(self, num):
        result = self.octal_to_binary(num)
        return self.binary_to_decimal(result)
    
    
    def list_generator(self, output_type):
        nums = []
        if output_type == 'octal':
            for i in range(1, 1000):
                nums.append(self.decimal_to_octal(i))  
        elif output_type == 'hex':
            for i in range(1, 1000):
                nums.append(self.decimal_to_hex(i))      
        else:
            for i in range(1, 1000):
                nums.append(self.decimal_to_binary(i))             
        return nums    
            
#print(Zahlensysteme().list_generator('binary'))            