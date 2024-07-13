class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=''
        for val in zip(*strs):
            if val.count(val[0])==len(val):
                res+=val[0]
            else:
                break
        return res
