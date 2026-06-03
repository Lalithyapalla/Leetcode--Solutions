class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        r = t
        for char in s:
            if char in t:
                r = r.replace(char,'',1)
        for char in r:
            if char in t:
                t = t.replace(char,'',1)
        return t == s
