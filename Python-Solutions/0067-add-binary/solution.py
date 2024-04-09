class Solution:
    def binary(self,num,pos=0):
            if num==0:
                return 0
            return num%10*(2**pos)+self.binary(num//10,pos+1)
    def addBinary(self, a: str, b: str) -> str:
        res=self.binary(int(a))+self.binary(int(b))
        return bin(res)[2:]
