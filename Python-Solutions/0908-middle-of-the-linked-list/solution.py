# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """cur = head
        l = 0
        while cur!= None:
            cur = cur.next
            l += 1
        cur = head
        for i in range(l//2):
            cur = cur.next
        return cur
        """
        slow = head
        fast = head
        while fast != None and fast.next != None :
            slow = slow.next
            fast = fast.next.next
        return slow

