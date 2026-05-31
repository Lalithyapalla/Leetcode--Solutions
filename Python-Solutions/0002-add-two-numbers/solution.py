# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        cur = head
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            val1 = l1.val if l1 != None else 0
            val2 = l2.val if l2 != None else 0
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10                         
            newnode = ListNode(digit)
            if head == None:
                head = newnode
                cur = head
            else:
                cur.next = newnode
                cur = cur.next
                
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
                
        return head
