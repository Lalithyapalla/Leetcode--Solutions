class Solution:
    def conversion(self, num):
        return (self.conversion(num // 7) if num >= 7 else '') + str(num%7)
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        if num > 0:
            return self.conversion(num)
        else:
            return '-' + self.conversion(abs(num))

