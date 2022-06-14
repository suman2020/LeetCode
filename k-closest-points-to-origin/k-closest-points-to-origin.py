class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # https://www.youtube.com/watch?v=rI2EBUEMfTk
        # https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/
        # https://www.geeksforgeeks.org/min-heap-in-python/
        
        minHeap = []
        for x,y in points:
            dist = (x**2) + (y **2)
            
            minHeap.append([dist,x,y])
            
        
        heapq.heapify(minHeap)
        res = []
        
        while k>0:
            dist,x,y  = heapq.heappop(minHeap)
            res.append([x,y])
            k -=1
            
        return res
    
        
        # Time complexity: k.logn (logn--> retrieve/pop)