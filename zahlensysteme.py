class Zahlensysteme:
    def __init__(self):
        pass
        
        
    def binary_to_decimal(self, num):
        sum = 0
        binary_nums = [1]
        for i in range(1, len(num)):
            binary_nums.append(2**i) 
        for i in range(len(num)):
            sum += int(num[::-1][i]) * binary_nums[i]
        return sum            
    
    
    def decimal_to_binary(self,num):  
        return bin(int(num)).replace("0b", "")
    
    
    def octal_to_binary(self,octnum): 
        binary = ""  # initialising bin as String
        octnum = int(octnum)
        # While loop to extract each digit
        while octnum != 0:
            
            # extracting each digit
            d = int(octnum % 10)
            if d == 0:
                
                # concatenation of string using join function
                binary = "".join(["000", binary])
            elif d == 1:
                
                # concatenation of string using join function
                binary = "".join(["001", binary])
            elif d == 2:
                
                # concatenation of string using join function
                binary = "".join(["010", binary])
            elif d == 3:
                
                # concatenation of string using join function
                binary = "".join(["011", binary])
            elif d == 4:
                
                # concatenation of string using join function
                binary = "".join(["100", binary])
            elif d == 5:
                
                # concatenation of string using join function
                binary = "".join(["101", binary])
            elif d == 6:
                
                # concatenation of string using join function
                binary = "".join(["110",binary])
            elif d == 7:
                
                # concatenation of string using join function
                binary = "".join(["111", binary])
            else:
                
                # an option for invalid input
                binary = "Invalid Octal Digit"
                break
    
            # updating the oct for while loop
            octnum = int(octnum / 10)
            
        # returning the string binary that stores
        # binary equivalent of the number
        return binary
    
    
    def binary_to_octal(self, num):
        # create Map 
        bin_to_oct_dict = {"000":'0', "001":'1', "010":'2', "011":'3', 
                           "100" : '4', "101" : '5', "110" : '6', "111" : '7' }
        # add min 0's in the beginning to make
        # left substring length divisible by 3
        for _ in range(1, (3 - len(str(num)) % 3) % 3 + 1):
            num = '0' + num    
        i = 0 
        octal = '0' 
        while True:
            # of size 3 and add its octal code
            octal += bin_to_oct_dict[num[i:i + 3]]
            i += 3
            if (i == len(num)):
                break
        # required octal number
        return octal
        
   
    def hex_to_decimal(self,num):
        hex_dict = {'0': 0, '1' : 1, '2' : 2, '3' : 3, 
         '4' : 4, '5' : 5, '6' : 6, '7' : 7, 
         '8' : 8, '9' : 9, 'A' : 10 , 'B' : 11, 
         'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15, 'a' : 10 , 'b' : 11, 
         'c' : 12, 'd' : 13, 'e' : 14, 'f' : 15}  
        result = ''
        for i in str(num):
            result += str(hex_dict[i]) 
        return result    
    
    
    def decimal_to_hex(self, num):
        return str(hex(int(num)))[2:]
    
    
    def hex_to_binary(self,num):
        num = self.hex_to_decimal(num)
        return self.decimal_to_binary(num)


    def binary_to_hex(self, num):
        num = self.binary_to_decimal(num)
        return self.decimal_to_hex(num)    
    
    
    def octal_to_hexa(self, num): 
        result = self.octal_to_binary(num)
        return self.binary_to_hex(result)
    
    
    def hex_to_octal(self, num):
        num = self.hex_to_binary(num) 
        return self.binary_to_octal(num)   

    
    def decimal_to_octal(self, num):
        result = self.decimal_to_binary(num)
        return self.binary_to_octal(result)
    
    
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