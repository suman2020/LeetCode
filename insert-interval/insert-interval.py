class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
    
        
        # https://www.youtube.com/watch?v=A8NUOmlwOlM
        
        ROWS = len(intervals)
        
        ans = []
        
        if ROWS==0:
            ans.append(newInterval)
            return ans
            
        
        for i in range(ROWS):
            
            
                
            if newInterval[1] < intervals[i][0]:
                ans.append(newInterval)
                return ans + intervals[i:]
                
            elif newInterval[0] > intervals[i][1]:
                ans.append(intervals[i])
                
            else:
                left_bnd = min(newInterval[0],intervals[i][0])
                right_bnd = max(newInterval[1], intervals[i][1])
                newInterval = [left_bnd, right_bnd]
        ans.append(newInterval)
                
        return ans
                
            
            
        
        