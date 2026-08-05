# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        if not head:
            return None
        def reverse(node, node_prev = None): 
            nonlocal res
            if node.next == None:
                res = node
                node.next = node_prev
                return
            reverse(node.next, node)
            node.next = node_prev
        reverse(head)
        return res

            


        