class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new=s.strip()
        return len(new.split()[-1])
