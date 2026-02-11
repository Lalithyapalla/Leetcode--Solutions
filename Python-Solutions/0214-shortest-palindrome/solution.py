class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        rev = s[::-1]
        for i in range(len(s), -1, -1):
            if s[:i] == rev[len(s)-i:]:
                return rev[:len(s)-i] + s
      
