# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = head
        right_prev = None
        right = head
        count = 0



        while left.next:
            left = left.next
            count += 1
            if count >= n:
                right_prev = right
                right = right.next
        if not right_prev:
            head = head.next
            return head
        right_prev.next = right.next
        return head
        
        