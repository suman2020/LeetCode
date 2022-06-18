# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # https://www.youtube.com/watch?v=1UOPsfP85V4
        
        dummyNode = ListNode(0,head)
         
        groupPrev = dummyNode # pointer right before start of group
        
        
        while True:
            kthNode = self.getKthNode(groupPrev,k)
            
            if not kthNode: #last group 1-2-3-4-5, k= 2, 5 doesnot have a pair, so we break out of loop
                break
            
            groupNext = kthNode.next # 1-2-3-4-5, k= 2, our grouNext will point at 3 now at first iteration
            
            # reverse the group
            prev = kthNode.next
            curr = groupPrev.next
            
            while curr !=groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                
            tmp = groupPrev.next
            groupPrev.next = kthNode
            groupPrev = tmp
            
            
        return dummyNode.next
            
            
            
    # this function returns the node at k=2         
    def getKthNode(self, curr,k):
        
        while curr and k>0:
            k-=1
            curr = curr.next
            
        return curr
        
            
            
        