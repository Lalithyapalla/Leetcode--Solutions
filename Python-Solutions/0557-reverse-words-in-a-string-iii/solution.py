class Solution:
    def reverseWords(self, s: str) -> str:
        list1 = s.split()
        res = ''
        word = ''
        for char in s:
            if char !=' ':
                word = char + word
            else:
                res += word + ' '
                word = ''
        return res + word
