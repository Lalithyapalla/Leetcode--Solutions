class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        caps = sum(1 for char in word if char.isupper())
        if len(word) == caps or caps == 0:
            return True
        if caps == 1 and word[0].isupper():
            return True
        return False