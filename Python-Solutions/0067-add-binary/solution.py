class Solution:
    # def binary(self,num,pos=0):
    #         if num==0:
    #             return 0
    #         return num%10*(2**pos)+self.binary(num//10,pos+1)
    # def addBinary(self, a: str, b: str) -> str:
    #     res=self.binary(int(a))+self.binary(int(b))
    #     return bin(res)[2:]

    def binary(self,a,pos=0):
        if a==0:
            return 0
        return (a%10)*(2**pos)+self.binary(a//10,pos+1)
    def addBinary(self, a: str, b: str) -> str:
        res=self.binary(int(a))+self.binary(int(b))
        return self.convert_dec(res)
    
    def convert_dec(self,num): 
        if num==0:
            return '0'
        res=''
        while num>0:
            val=num%2
            res=str(val)+res
            num//=2
        return res

