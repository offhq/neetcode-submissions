# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        left_prev = dummy
        left_curr = dummy
        right_curr = dummy
        fast = dummy
        pos = 0
        while fast:
            fast = fast.next
            pos += 1
            if pos <= right:
                right_curr = right_curr.next
            if pos <= left:
                left_prev = left_curr
                left_curr = left_curr.next
        left_prev.next = None
        connect = right_curr.next
        right_curr.next = None
        
        prev = None
        curr = left_curr
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        left_prev.next = prev
        left_curr.next = connect



        return dummy.next