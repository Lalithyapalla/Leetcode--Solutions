class Solution:
    def firstUniqChar(self, s: str) -> int:
        """d = {}
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1"""

        min_index = len(s)
        for char in "abcdefghijklmnopqrstuvwxyz":
            first = s.find(char)
            if first != -1 and first == s.rfind(char):
                if first < min_index:
                    min_index = first
        return min_index if min_index < len(s) else -1
