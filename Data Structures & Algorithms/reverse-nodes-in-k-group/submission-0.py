# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        section_end = dummy
        curr = dummy.next
        section_start = dummy.next
        i = 0
        while curr:
            i += 1
            if i == k:
                connect = curr.next
                curr.next = None
                s = self.reverseList(section_start)
                section_end.next = s
                section_end = section_start
                section_start.next = connect
                section_start = section_start.next
                i = 0
                curr = section_end
            curr = curr.next

        return dummy.next
