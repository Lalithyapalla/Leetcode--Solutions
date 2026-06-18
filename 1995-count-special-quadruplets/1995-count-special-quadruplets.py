class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n, ans = len(nums), 0
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                for k in range(j + 1, n - 1):
                    s = nums[i] + nums[j] + nums[k]
                    for a in range(k + 1, n):
                        if nums[a] == s:
                            ans += 1
        return ans