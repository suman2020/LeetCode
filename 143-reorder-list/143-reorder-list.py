# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # https://www.youtube.com/watch?v=S5bfdUTrKLM
        
        # finding the mid point
        slow, fast = head, head.next
        count =1
        while fast and fast.next:   
            count+=1
        
            slow = slow.next
            fast = fast.next.next
        print(count)
            
        second = slow.next
        
        slow.next = prev =  None
        
        # reversing second half
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
            
        # merge two halfs
        first,second = head, prev
        
        while second:
            temp1,temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first,second = temp1, temp2
            
            
            