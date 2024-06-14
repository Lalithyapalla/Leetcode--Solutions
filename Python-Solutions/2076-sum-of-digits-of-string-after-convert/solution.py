class Solution:
    def getLucky(self, s: str, k: int) -> int:
        dig=''
        for char in s:
            dig+=str(26-(122-ord(char)))
        for _ in range(k):
            sum=0
            for ele in dig:
                sum+=int(ele)
            dig=str(sum)
            #print(sum)
        return sum
