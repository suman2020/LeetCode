class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        # https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/952714/Two-solutions-based-on-MergeSort-EXPLAINED
        
        n = len(nums)
        enum = [(i,v) for i,v in enumerate(nums)] # record value and index
        # [[5, 0], [2, 1], [6, 2], [1, 3]]

        res = [0]*n  # return array
        
        
        self.mergeSort(enum,0,n-1, res)
        
        return res
    
    
    def mergeSort(self,enum,start,end,res):
        if start>=end:
            return
        
        mid = (end+start)//2
        
        self.mergeSort(enum,start,mid,res)
        self.mergeSort(enum,mid+1,end,res)
        self.merge(enum,start,mid,end,res)
        
        
    def merge(self,enum,start,mid,end,res):
        p,q = start,mid+1
        
        count = 0
        
        temp = []
        
        while p<=mid and q<=end:
            if enum[p][1] <=enum[q][1]:
                temp.append(enum[p])
                res[enum[p][0]] += count
                p+=1
                
            else:
                temp.append(enum[q])
                count+=1
                q+=1
        
        while p<=mid:
            temp.append(enum[p])
            res[enum[p][0]] += count
            p+=1
            
        while q<=end:
            temp.append(enum[q])
            q+=1
            
        enum[start:end+1] = temp
        
        
        
    
            
        