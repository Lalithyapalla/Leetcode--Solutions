class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
                                    
        sgn = 1
        i = 0
        if s[0] == '-':
            sgn = -1
            i += 1
        elif s[0] == '+':
            i += 1
        r = 0
        while i < len(s) and s[i].isdigit():
            r = r * 10 + int(s[i])
            i += 1
        r *= sgn
        mx = 1 << 30
        mx *= 2
                        
        if r < -mx:
            return -mx
        if r > mx - 1:
            return mx - 1
        return r

