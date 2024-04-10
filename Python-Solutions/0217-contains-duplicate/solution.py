class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #res=list(filter(lambda num:nums.count(num)>1,nums))
        res=set(nums)
        if len(res)==len(nums):
            return False
        else:
            return True

