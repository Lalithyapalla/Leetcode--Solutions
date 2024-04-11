class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        #res=list(set(filter(lambda val:val<0,nums)))+list(set(filter(lambda val:val>=0,nums)))
        a1=list(filter(lambda val:val<0,nums))
        a2=list(filter(lambda val:val>=0,nums))
        a1.sort()
        a2.sort()
        result=a1+a2
        res=list(set(result))
        res.sort()
        #print(res)
        if len(res)>2:
            return res[-3]
        else:
            return res[-1]

