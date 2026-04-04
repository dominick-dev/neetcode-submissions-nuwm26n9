# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        d1, d2 = list1, list2
        curr = ListNode(0, None)
        start = curr

        while d1 and d2:
            if d1.val < d2.val:
                curr.next = ListNode(d1.val, None)
                d1 = d1.next
            else:
                curr.next = ListNode(d2.val, None)
                d2 = d2.next

            curr = curr.next
        
        if d1:
            curr.next = d1

        if d2:
            curr.next = d2

        return start.next
            
