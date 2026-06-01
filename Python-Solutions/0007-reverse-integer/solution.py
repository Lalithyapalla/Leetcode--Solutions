class Solution:
    def reverse(self, x: int) -> int:
        s = -1 if x < 0 else 1
        x, r = abs(x), 0
                
        while x:
            r = (r * 10) + (x % 10)
            x //= 10
        r *= s
        return r if -2**31 <= r <= 2**31 - 1 else 0
