class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        res = {}
        for num in arr:
            if num not in res:
                res[num] = 1
            else:
                res[num] += 1
                #{1:3,2:2,3:2}
        return len(res.values()) == len(set(res.values()))