class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=list(filter(lambda val:nums.count(val)==1,nums))
        return res[0] 
