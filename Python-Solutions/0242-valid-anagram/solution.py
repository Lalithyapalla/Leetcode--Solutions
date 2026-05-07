class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd={}
        td={}
        count=1
        for l in s:
            if l not in sd:
                sd[l]=count
                count=1
            else:
                sd[l]=sd[l]+1
        for l in t:
            if l not in td:
                td[l]=count
                count=1
            else:
                td[l]=td[l]+1

        if len(s)!=len(t):
            return False
        elif sd==td:
            return True
        else:
            return False
