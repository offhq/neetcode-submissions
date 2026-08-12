"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        htbl = {}
        dummy = Node(0)
        current_new = dummy
        current_old = head
        while current_old:
            current_new.next = Node(current_old.val)
            current_new = current_new.next
            htbl[current_old] = current_new
            current_old = current_old.next
        
        current_new_r = dummy
        current_old_r = head

        while current_old_r:
            current_new_r = current_new_r.next
            if current_old_r.random:
                current_new_r.random = htbl[current_old_r.random]
            current_old_r = current_old_r.next

        return dummy.next



        
        

            





        