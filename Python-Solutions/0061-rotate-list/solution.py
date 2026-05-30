# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        last = head
        cur = head
        l = 0
        while last.next != None:
            last = last.next
            l += 1
        last.next = head
        l += 1
        k = k % l
        for _ in range(l - k - 1):
            cur = cur.next
        head = cur.next
        cur.next = None
        return head
        
        
