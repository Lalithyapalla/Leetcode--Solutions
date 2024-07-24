class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
      val=0
      if needle not in haystack:
        return -1
      else:
        for st in range(len(haystack)):
            for ev in range(st+1,len(haystack)+1):
                if haystack[st:ev]==needle:
                    val=haystack.index(needle)
        return val 
    
