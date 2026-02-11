class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        # 1. Find the middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. Reverse the second half
        # MOVE PREV OUTSIDE THE FIRST LOOP
        prev = None 
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            
        # 3. Compare the halves
        left, right = head, prev
        while right: 
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        return True
