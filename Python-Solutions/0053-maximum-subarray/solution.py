class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        csum,maxsum=nums[0],nums[0]
        for i in range(1,len(nums)):
            csum=max(nums[i],csum+nums[i])
            maxsum=max(maxsum,csum)
        return maxsum

