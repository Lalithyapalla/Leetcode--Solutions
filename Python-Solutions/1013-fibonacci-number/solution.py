class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        prev2, prev1 = 0, 1
        for i in range(2, n + 1):
            cur = prev2 + prev1
            prev2 = prev1
            prev1 = cur
        return prev1
