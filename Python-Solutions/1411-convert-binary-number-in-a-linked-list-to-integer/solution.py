# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        cur = head
        size = 0
        if head == None or head.next == None:
            return head.val
        while cur != None:
            size += 1
            cur = cur.next
        cur = head
        value = 0
        while cur != None:
            value = (cur.val * (2 ** (size - 1))) + value
            size -= 1
            cur = cur.next
        return value
