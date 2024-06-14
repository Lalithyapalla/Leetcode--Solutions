class Solution:
    def countEven(self, num: int) -> int:
        def add(num):
            if num==0:
                return 0
            sum=0
            temp=num
            while temp>0:
                sum+=temp%10
                temp//=10
            return(sum%2==0)+add(num-1)
        return add(num)

