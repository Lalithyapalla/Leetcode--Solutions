class Solution:
    def averageValue(self, nums: List[int]) -> int:
        even = []
        for val in nums:
            if (val % 2 == 0) and (val % 3 == 0):
                even.append(val)
        return (sum(even) // len(even)) if sum(even) > 0 else 0