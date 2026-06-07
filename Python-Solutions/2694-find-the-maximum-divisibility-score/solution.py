class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        d ={}
        for div in divisors:
            c=0
            for num in nums:
                if num%div == 0:
                    c+=1
            d[div] = c
        max_s=0
        new = {}
        for i in d:
            if d[i] not in new:
                new[d[i]]=1
            else:
                new[d[i]] += 1
            if d[i] > max_s:
                max_s = d[i]
        ans =[]
        for val in d:
            if d[val] == max_s:
                ans.append(val)
        return min(ans)

