class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        
        # 1. Collect all values from all linked lists
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        
        # 2. Sort the values
        nodes.sort()
        
        # 3. Create a new linked list from the sorted values
        dummy = ListNode(0)
        current = dummy
        
        for val in nodes:
            current.next = ListNode(val)
            current = current.next
            
        return dummy.next
