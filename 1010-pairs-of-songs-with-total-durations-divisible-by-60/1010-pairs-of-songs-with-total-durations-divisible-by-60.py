class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # https://www.youtube.com/watch?v=UcCBdYQU2cU
        temp_dict = {}
        totalPairs = 0
        
        for num in time:
            modNum = num %60
            if modNum == 0:
                if 0 in temp_dict:
                    totalPairs +=temp_dict[0]

            elif (60-modNum) in temp_dict:
                totalPairs +=temp_dict[60-modNum]


            if modNum in temp_dict:
                temp_dict[modNum] +=1

            else:
                temp_dict[modNum] = 1
        
        return totalPairs
        
        
        
        """
        30 20 150 100 40 0 60 60 30 30 40 20
        
            temp_dict = {}
            - 30%60 = 30, 60-30=30 in dict: No
              temp_dict= {30:1}
              
            - 20%60 = 20, 60-20 = 40 in dict: No
              temp_dict= {30:1, 20:1}
             
             - 150%60 = 30, 60-30=30 in dict: Yes
                totalpairs= 1
              
              temp_dict= {30:2, 20:1}
              
             - 100%60 = 40, 60-40=20 in dict: Yes
                totalpairs = 2
              temp_dict= {30:2,20:1,40:1}
              
             - 40%60 = 40, 60-40=20 in dict: Yes
                totalpairs = 2+1 = 3
              temp_dict= {30:2,20:1,40:2}
              
              - 0%60 = 0, 60-0 in dict:No
              temp_dict= {30:2,20:1,40:2,0:1}
              
              - 60%60 = 0, 60-0=0 in dict: Yes
                totalpairs = 3+1 = 4
               temp_dict= {30:2,20:1,40:2,0:2}
               
               - 60%60 = 0, 60-0=0 in dict: Yes
                totalpairs = 4+2 = 6
               temp_dict= {30:2,20:1,40:2,0:2}
               
               - 30%60 = 0, 60-30=0 in dict: Yes
                totalpairs = 6+2 = 8
               temp_dict= {30:3,20:1,40:2,0:2}
               
               
               
              
              
              
              
        
        
        """
    
    

    
    