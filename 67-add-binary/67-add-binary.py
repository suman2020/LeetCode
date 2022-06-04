class Solution:
    def addBinary(self, a: str, b: str) -> str:
        y = int(a)  #11
        x = int(b)   #1
        y1 = int(a,2)#3
        x1 = int(b,2)#1
        print(y)
        print(x)
        print(y1)
        print(x1)
        
        sum_ = bin(int(a,2) + int(b,2))
        
        return sum_[2:]
        