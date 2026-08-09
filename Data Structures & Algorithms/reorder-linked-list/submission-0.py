# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverseList(node):
            prev = None
            curr = node
            
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        
        curr = head
        while curr:
            next_node = reverseList(curr.next)
            curr.next = next_node
            curr = curr.next
    

        
        
        