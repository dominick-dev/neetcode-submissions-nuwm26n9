# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, 0)
        start = dummy
        carry = 0

        while l1 and l2:
            curr_sum = l1.val + l2.val + carry
            if curr_sum > 9:
                carry = 1
                curr_sum %= 10
            else:
                carry = 0

            new_node = ListNode(curr_sum, None)
            dummy.next = new_node
            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            if carry:
                curr_sum = l1.val + carry
                if curr_sum > 9:
                    carry = 1
                    curr_sum %= 10
                else:
                    carry = 0

                new_node = ListNode(curr_sum, None)
                dummy.next = new_node
                dummy = dummy.next
                l1 = l1.next
            else:
                dummy.next = l1
                break

            
        while l2:
            if carry:
                curr_sum = l2.val + carry
                if curr_sum > 9:
                    carry = 1
                    curr_sum %= 10
                else:
                    carry = 0

                new_node = ListNode(curr_sum, None)
                dummy.next = new_node
                dummy = dummy.next
                l2 = l2.next
            else:
                dummy.next = l2
                break

        if carry:
            new_node = ListNode(carry, None)
            dummy.next = new_node
            dummy = dummy.next
        
        return start.next
        