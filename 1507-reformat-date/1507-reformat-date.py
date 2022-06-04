class Solution:
    def reformatDate(self, date: str) -> str:
        
        dict_ ={"Jan":'01', "Feb":'02', "Mar":'03', "Apr":'04', "May":'05', "Jun":'06', "Jul":'07', "Aug":'08', "Sep":'09', "Oct":'10', "Nov":'11', "Dec":'12' }
        
        list_ = date.split()
        
        
        # extracting day
        i = 0
        day_=''
        while list_[0][i].isdigit():
            day_ = day_ + list_[0][i]
            i+=1
           
        if i==1:
            day_ = '-0'+ day_
        else:
            day_ = '-'+day_
        
        month = '-' + dict_[list_[1]]
        
        year = list_[2]
        
        return year + month + day_
        
        
            
                
                
            