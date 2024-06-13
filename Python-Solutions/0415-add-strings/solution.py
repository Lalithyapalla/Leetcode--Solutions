class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        pow=''
        new=0
        if len(num1)>len(num2):
            n22='0'* (len(num1) - len(num2))+num2
            n11=num1    
        elif len(num1)<len(num2):
            n11='0'* (len(num2) - len(num1))+num1
            n22=num2
        else:
            n11,n22=num1,num2
        for ind in range(len(n11)-1,-1,-1):
            a=n11[ind]
            b=n22[ind]
            new=new+int(a)+int(b)
            if new>9:
                pow+=str(new)[-1]
                new=int(str(new)[0])
            else:
                pow+=str(new)
                new=0
        if new != 0:
            pow += str(new)
        return pow[::-1]
