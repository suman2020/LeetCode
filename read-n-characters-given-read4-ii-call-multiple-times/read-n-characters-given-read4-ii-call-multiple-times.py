# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    
    """
    read4--> reads 4 characters from the file
    buf4 --> stores the read characters by the read4 method (at most 4 characters in each call of read4 method)
    queue --> add the elements stored in buf4 to the queue
    
    pop the elements from the queue as desired
    
    """
    
    def __init__(self):
        self.queue = collections.deque()
    
    def read(self, buf: List[str], n: int) -> int:
        
        buf4 = ['']*4
        total_read_so_far = 0
        
        while total_read_so_far < n:
            
            # read 4 characters from the file
            v = read4(buf4)
            
            total_read_so_far +=v
            
            
            
            # add only the read chracters into our queue
            self.queue.extend(buf4[:v])
            
            # if no characters to read: end of line, exit of while loop
            if v==0:
                break
                
                
        i = 0
        
        
        
        while i<n and self.queue:
            buf[i] = self.queue.popleft()
            i+=1
            
        
        return i
    
            
            
                
        
        