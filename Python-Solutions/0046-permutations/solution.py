class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(start):
        # Base case: we've swapped everything to a valid position
            if start == len(nums):
                res.append(nums[:])
                return
            
            for i in range(start, len(nums)):
                # Swap the current element with the start
                nums[start], nums[i] = nums[i], nums[start]
                # Recurse for the next position
                backtrack(start + 1)
                # Backtrack (swap back) to restore the list
                nums[start], nums[i] = nums[i], nums[start]
            
        backtrack(0)
        return res
