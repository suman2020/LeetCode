class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        
        # https://www.youtube.com/watch?v=5r03fZzUPFA
        
        workers = [[w/q, q] for q, w in zip(quality, wage)]
        workers.sort()  # sort in increasing order by ratio
        
        maxHeap = []
        totalQuality = 0
        minCost = float('inf')
        
        for ratio, q in workers:
            
            # Store negative of quality for max heap
            heapq.heappush(maxHeap, -q) # maxHeap on the basis of quality
            
            totalQuality += q
            
            if len(maxHeap)>k:
                # Storing negative values for quality
                # so, on popping max value, we get quality to subtract
                # from current total quality
                totalQuality+=heapq.heappop(maxHeap)
                
            if len(maxHeap)==k:
                # If there are current K items in max
                # heap of qualities, calculate the
                # cost to hire these workers at rate of
                # current worker's ratio. Because the ratios are sorted
				# we are here trying to get min cost for max quality
                minCost = min(minCost, totalQuality * ratio)
                
            
        return minCost
        
        