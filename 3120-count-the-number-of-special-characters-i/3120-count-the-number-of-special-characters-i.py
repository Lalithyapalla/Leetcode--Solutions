class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word = list(set(word))
        count = 0
        for char in word:
            if char.islower():
                if char.upper() in word:
                    count += 1
        return count