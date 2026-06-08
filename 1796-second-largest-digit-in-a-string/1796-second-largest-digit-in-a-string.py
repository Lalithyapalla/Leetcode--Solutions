class Solution:
    def secondHighest(self, s: str) -> int:
        s = list(set(s))
        l = []
        for char in s:
            if 97 <= ord(char) <= 122:
                continue
            else:
                l.append(int(char))
        l = sorted(list(set(l)))
        if len(l) < 2:
            return -1
        else:
            return l[-2]