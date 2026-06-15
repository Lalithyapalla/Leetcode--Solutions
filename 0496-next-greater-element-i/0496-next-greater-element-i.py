class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nxt_greater = {}
        stack = []
        
        for num in nums2:
            while stack and stack[-1] < num:
                nxt_greater[stack.pop()] = num
            stack.append(num)
            
        while stack:
            nxt_greater[stack.pop()] = -1
            
        return [nxt_greater[num] for num in nums1]