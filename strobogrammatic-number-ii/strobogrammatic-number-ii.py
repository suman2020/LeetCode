class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        #https://www.geeksforgeeks.org/strobogrammatic-number/
        
        def build(num):
            if not num:
                return []
            if num==1: return ["1","0","8"]
            
            middles = build(num-2)
            result = []
            
            if not middles:
                middles.append('')
            
            for middle in middles:
                
                if num!=n:
                    result.append('0'+middle+'0')
                
                result.append('1'+middle+'1')
                result.append('8'+middle+'8')
                result.append('9'+middle+'6')
                result.append('6'+middle+'9')
                
            return result   
        return build(n)
        