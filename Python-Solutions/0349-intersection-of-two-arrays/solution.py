class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=set(list(filter(lambda val:val in nums2,nums1)))
        return res
