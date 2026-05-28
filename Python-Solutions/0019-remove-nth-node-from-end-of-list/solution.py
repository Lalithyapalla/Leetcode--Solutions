# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """cur = head
        l = 0
        while cur != None:
            cur = cur.next
            l += 1
        if l == n:
            return head.next
        cur = head
        for i in range(l - n - 1):
            cur = cur.next
        cur.next = cur.next.next
        return head"""
        p1 = p2 = head
        for i in range(n):
            p2 = p2.next
        if p2 is None:
            return head.next
        while p2.next!= None:
            p1 = p1.next
            p2 = p2.next
        p1.next = p1.next.next
        return head
        
