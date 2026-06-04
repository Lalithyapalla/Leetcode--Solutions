class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        l = s.split()
        res = []
        for word in l:
           res = [word] + res
        return " ".join(res)

  
