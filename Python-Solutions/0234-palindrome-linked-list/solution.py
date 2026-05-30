class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        l = []
        while cur != None:
            l.append(cur.val)
            cur = cur.next
        return l == l[::-1]
        """if head == None or head.next == None:
            return True
        fwdlist = self.display(head)
        rvslist = self.reverse(head)
        bcklist = self.display(rvslist)
        return fwdlist == bcklist
    def display(self,head):
        l1 = []
        cur = head
        while cur != None:
            l1.append(cur.val)
            cur = cur.next
        return l1
    def reverse(self,head):
        cur = head
        prev = nxt = None
        while cur != None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
            """
       
