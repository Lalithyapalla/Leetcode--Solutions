class Solution:
    def toLowerCase(self, s: str) -> str:
        res = ''
        for char in s:   
            if 65 <= ord(char) <= 90:
                res += chr(ord(char) + 32)
            else:
                res += char
        return res
