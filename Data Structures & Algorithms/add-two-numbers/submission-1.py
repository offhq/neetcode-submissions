# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        lsum = dummy
        while l1 and l2:
            digit = l1.val + l2.val
            if carry == 1:
                digit += 1
                carry = 0
            if digit >= 10:
                digit = digit%10
                carry = 1
            lsum.next = ListNode(digit)
            lsum = lsum.next
            l1, l2 = l1.next, l2.next

        if l1:
            while l1:
                digit = l1.val
                if carry == 1:
                    digit += 1
                    carry = 0
                if digit >= 10:
                    digit = digit % 10
                    carry = 1
                lsum.next = ListNode(digit)
                lsum = lsum.next
                l1 = l1.next
        elif l2:
            while l2:
                digit = l2.val
                if carry == 1:
                    digit += 1
                    carry = 0
                if digit >= 10:
                    digit = digit % 10
                    carry = 1
                lsum.next = ListNode(digit)
                lsum = lsum.next
                l2 = l2.next
                
                


                 
        if carry == 1:
            lsum.next = ListNode(1)
        return dummy.next

            



