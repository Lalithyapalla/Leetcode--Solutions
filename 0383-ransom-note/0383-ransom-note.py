class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
       
        ans = {char: magazine.count(char) for char in set(magazine)}
        for char in ransomNote:
            if char in ans and ans[char] > 0 :
                ans[char] -= 1
            else:
                return False
        return True