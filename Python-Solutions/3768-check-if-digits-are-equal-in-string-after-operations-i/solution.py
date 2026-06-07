class Solution:
    def hasSameDigits(self, s: str) -> bool:
        dig = [int(x) for x in s]
        while len(dig) > 2:
            res = []
            for i in range(len(dig)-1):
                res.append((dig[i] + dig[i+1]) % 10)
            dig = res
        return dig[0]==dig[-1]
            

