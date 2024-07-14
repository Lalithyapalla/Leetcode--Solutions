class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return {char:s.count(char) for char in s}=={char:t.count(char) for char in t}
    #     l=len(s)
    #    # l1=len(t)
    #     c=0
    #     if len(s)==len(t):
    #         for ch in s:
    #             if ch in t:
    #                 c+=1
    #                 s=s.replace(ch,'',1)
    #                 t=t.replace(ch,'',1)

    #         return c==l
    #     return False

            
