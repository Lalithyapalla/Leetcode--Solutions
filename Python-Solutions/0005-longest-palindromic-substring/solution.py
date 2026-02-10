class Solution:
    def longestPalindrome(self, s: str) -> str:
        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                substring = s[start : start + length]
                if substring == substring[::-1]:
                    return substring
        return ""
