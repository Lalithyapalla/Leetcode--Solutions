class Solution:
    def isPalindrome(self, x: int) -> bool:
        # new=str(x)
        # s=''
        # for ind in range(len(new)-1,-1,-1):
        #     s+=new[ind]
        # return s==new

        # x=str(x)
        # if int(x)<0:
        #     return False
        # li,ri=0,len(x)-1
        # flag=False
        # while(li<=ri):
        #     if x[li]!=x[ri]:
        #         return False
        #     elif x[li]==x[ri]:
        #         li+=1
        #         ri-=1
        #         flag=True
        # return flag

        return str(x)==str(x)[::-1]
