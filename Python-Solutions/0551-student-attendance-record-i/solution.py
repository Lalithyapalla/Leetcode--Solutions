class Solution:
    def checkRecord(self, s: str) -> bool:
        award = False
        if s.count('A') < 2:
            award = True
            for i in range(len(s)-2):
                if s[i] == s[i+1] == s[i+2] == 'L':
                    award = False
                    return award
                else:
                    award = True
        return award

