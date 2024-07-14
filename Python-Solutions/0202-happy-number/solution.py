class Solution:
    def isHappy(self, n: int) -> bool:
        dsum=self.sq_num(n)
        if dsum>9:
            return self.isHappy(dsum)
        else:
            if dsum==1 or dsum==7:
                return True
            else:
                return False
    def sq_num(self,n):
        if n==0:
            return 0
        return ((n%10)**2)+self.sq_num(n//10)
    
