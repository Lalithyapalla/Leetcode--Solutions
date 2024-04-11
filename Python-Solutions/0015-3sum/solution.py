class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for ind1 in range(len(nums)-2):
            if ind1 > 0 and nums[ind1] == nums[ind1-1]:
                continue
            num1 = nums[ind1]
            ind2 = ind1+1
            ind3 = len(nums)-1
            while ind2 < ind3:
                num2 = nums[ind2]
                num3 = nums[ind3]
                s = num1 + num2 + num3
                if s == 0:
                    ans.append([num1, num2, num3])
                    while ind2 < ind3 and nums[ind2] == nums[ind2+1]:
                        ind2 += 1
                    while ind2 < ind3 and nums[ind3] == nums[ind3-1]:
                        ind3 -= 1
                    ind2 += 1
                    ind3 -= 1
                elif s > 0:
                    ind3 -= 1
                else:
                    ind2 += 1
        return ans
