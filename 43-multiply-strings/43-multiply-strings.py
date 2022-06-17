class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        # Time complexity: O(n*m)
        # Space complexity: O(n+m)
        # https://www.youtube.com/watch?v=1vZswirL8Y8&t=702s
        
        if num1=="0" or num2=="0":
            return "0"
        
        #99 * 99 = 9801(4 digits)
        # 999 * 99 = 98901 (5 digits)
        # max_length = m + n
        res = [0]*(len(num1) + len(num2)) # maximum length of string
        
        # we multiply in reverse order, so reversing the string
        num1,num2 = num1[::-1], num2[::-1]
        
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                
                digit = int(num1[i1])*int(num2[i2])
                
                res[i1+i2] += digit
                
                
            
                res[i1+i2+1] += (res[i1+i2]//10)  # carry
                
                res[i1+i2] = res[i1+i2] %10  # left over
                
        # 10 * 10 = [0,0,1,0] =. [0,1,0,0] 
        # we have leading zeros, so have to take care of such cases. 
        
        
        res = res[::-1]
        
        beg = 0
        while beg<len(res) and res[beg]==0:
            beg+=1
            
        res = res[beg:]
        print(res)
        res = [str(num) for num in res]
        
        return "".join(res)
                
                
        
                
        
        
        
        