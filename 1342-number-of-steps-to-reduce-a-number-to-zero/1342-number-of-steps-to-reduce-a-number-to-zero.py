class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        for i in range(num + 1):
            if num == 0:
                return count
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            count+= 1
            
        