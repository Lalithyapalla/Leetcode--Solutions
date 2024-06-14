class Solution:
    def alternateDigitSum(self, n: int) -> int:
        new=str(n)
        pos=''
        neg=''
        pos_sum=neg_sum=0
        for dig in range(len(new)):
            if dig%2==0:
                pos+=new[dig]
            else:
                neg+=new[dig]
        for dig in pos:
            pos_sum+=int(dig)
        for dig in neg:
            neg_sum+=int(dig)
        return pos_sum-neg_sum
