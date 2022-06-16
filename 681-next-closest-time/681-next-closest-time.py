class Solution:
    def nextClosestTime(self, time: str) -> str:
        
        hour,minute = time.split(":") # [19:34]
        
        print(hour) # 19
        
        temp_set =set(hour) 
        print(temp_set) # {1, 9 }
        
        nums = sorted(set(hour+minute))
        print(nums) # {1,3,4,9}
        
        
        def getAvailableTimes(nums):
            temp = []
            for outer_digit in nums:
                for inner_digit in nums:
                    temp.append(outer_digit+inner_digit)
                    
            return temp
        
        two_digit_values = getAvailableTimes(nums)
        print(two_digit_values)
        #['11', '13', '14', '19', '31', '33', '34', '39', '41', '43', '44', '49', '91', '93', '94', '99']
        
        # two_digit_values = [a+b for a in nums for b in nums]
        
    
            
        
        def getNextLargestMinute():
            index_of_minute = two_digit_values.index(minute)
            print(index_of_minute)
            if index_of_minute + 1 < len(two_digit_values):
                print("hello")
                if two_digit_values[index_of_minute+1] <"60":
                    return two_digit_values[index_of_minute + 1]
                
            return -1
                
                
        def getNextLargestHour():
            index_of_hour = two_digit_values.index(hour)
            if index_of_hour + 1 < len(two_digit_values):
                if two_digit_values[index_of_hour+1] <"24":
                    return two_digit_values[index_of_hour + 1]
                
            return -1
            
        # get the next largest minute if possible
        next_largest_minute = getNextLargestMinute()
        print(next_largest_minute)
        
        # if there is indeed a next largest minute, you are  all set, combine it with the given hour
        if next_largest_minute !=-1:
            return hour+":"+next_largest_minute
        
        else:
            minute = two_digit_values[0]
            next_largest_hour = getNextLargestHour()
            
            if next_largest_hour !=-1:
                return next_largest_hour+":"+minute
            else:
                return minute+":"+minute

        
        
        
        