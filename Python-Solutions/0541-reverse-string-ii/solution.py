class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        rem = ''  #  "abcdefg"
        res = ''
        if k == 1:
            return s
        while len(s) > 0:
            if len(s) >= 2*k :
                res += s[:k][::-1] + s[k:2*k]
                rem = s[2*k:]
                s = rem

            else:
                if len(s) >= k:
                    res += s[:k][::-1] + s[k:]
                else:
                    res += s[::-1]
                break
        return res


