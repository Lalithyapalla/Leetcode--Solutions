class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # res=list(filter(lambda fa:num%fa==0, range(1,num//2+1)))
        # div_sum=reduce(lambda a,b:a+b,res,0)
        # return div_sum==num
       if num<=1:
        return False
       n_sum=1
       for val in range(2,int(num**0.5)+1):
        if num%val==0:
            n_sum+=val
            if val!=num//val:
                n_sum+=num//val
       return n_sum==num

    # def perfect(self,num,fa=1):
    #     if fa==num:
    #         return 0
    #     return fa+self.perfect(num,fa+1) if (num%fa==0) else self.perfect(num,fa+1)

        
