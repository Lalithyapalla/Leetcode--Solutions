class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for i in range(n+1):
            string = str(bin(i))
            count = string.count('1')
            arr.append(count)
        return arr