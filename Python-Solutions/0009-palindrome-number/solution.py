class Solution:
    def isPalindrome(self, x: int) -> bool:
        new=str(x)
        s=''
        for ind in range(len(new)-1,-1,-1):
            s+=new[ind]
        return s==new
