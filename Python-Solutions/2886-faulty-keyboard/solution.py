class Solution:
    def finalString(self, s: str) -> str:
        res = ''
        for ele in s:
            if ele != 'i' :
                res += ele
            else:
                res = res[::-1]
        return res
