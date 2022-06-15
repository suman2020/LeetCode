class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # https://www.youtube.com/watch?v=FdzJmTCVyJU
        
        start = sorted([s for s,e in intervals])
        
        end = sorted([e for s,e in intervals])
        
        result, count = 0,0
        
        s,e = 0,0
        
        while s < len(intervals):
            if start[s] < end[e]:
                s+=1
                count +=1
                
                
            else:
                e+=1
                count -=1
                
            result = max(result,count)
            
            
        return result
    
        """
        [[0,30],[5,10],[10,20]]
        
        start = [0,5,15]
        end= [10,20,30]
        
        Step1:
            compare start_time(0) with end time (10):
                0<10--> count = 1, we need one room for this meeting
                
            compare start_time(5) with end time (10):
                5<10 --> count = 2, we need one more room., second meeting has started, but none of the meeting is ended
                
            compare start_time(10) with end_time(10):
                10<10: false --> count = 1, one room is open now cause a meeting just ended
                
            compare start_time(10) with end_time(15):
                10<15 --> we need one more room , so increment count = 2
        
        """
        
        