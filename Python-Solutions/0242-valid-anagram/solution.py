class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l=len(s)
       # l1=len(t)
        c=0
        if len(s)==len(t):
            for ch in s:
                if ch in t:
                    c+=1
                    s=s.replace(ch,'',1)
                    t=t.replace(ch,'',1)

            return c==l
        return False
            
