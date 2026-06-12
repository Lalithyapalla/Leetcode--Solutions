class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        hexmap = '0123456789abcdef'
        num %= 2 ** 32
        res = ""
        while num > 0:
            rem = num % 16
            res = hexmap[rem] + res
            num //= 16
        return res