class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[[val,ele] for val in range(len(nums)) for ele in range(val+1,len(nums)) if (nums[val]+nums[ele]==target)]
        return res[0]
