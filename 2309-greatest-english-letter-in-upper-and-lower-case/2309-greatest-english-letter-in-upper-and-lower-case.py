class Solution:
    def greatestLetter(self, s: str) -> str:
        word = list(set(s))
        count = []
        for char in word:
            if char.isupper():
                if char.lower() in word:
                    count.append(char)
        count = sorted(count)
        return count[-1] if len(count)>0 else ""