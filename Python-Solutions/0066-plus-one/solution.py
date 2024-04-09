class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new=''
        for num in digits:
            new+=str(num)
        res=int(new)+1
        a=list(map(int,str(res)))
        return a
