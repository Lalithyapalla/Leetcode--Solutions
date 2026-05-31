class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        prefix, suffix = p.split('*')
        i = s.find(prefix)
        if i == -1:
            return False
        return s.find(suffix, i + len(prefix)) != -1
