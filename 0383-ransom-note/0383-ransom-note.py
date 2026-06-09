class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_d = {char:magazine.count(char) for char in set(magazine) }
        for char in ransomNote:
            if char in mag_d and mag_d[char] > 0:
                mag_d[char] -= 1
            else:
                return False
        return True