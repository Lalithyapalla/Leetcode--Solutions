class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
       if num<=1:
        return False
       n_sum=1
       for val in range(2,int(num**0.5)+1):
        if num%val==0:
            n_sum+=val
            if val!=num//val:
                n_sum+=num//val
       return n_sum==num
