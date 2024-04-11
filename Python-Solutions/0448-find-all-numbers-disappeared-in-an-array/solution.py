class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length=len(nums)
        return list(set(range(1, length + 1)) - set(nums))
