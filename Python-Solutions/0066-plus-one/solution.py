class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # new=''
        # for num in digits:
        #     new+=str(num)
        # res=int(new)+1
        # a=list(map(int,str(res)))
        # return a

        string=reduce(lambda val1,val2:val1+str(val2), digits,'')
        #new=string[:-1]+str(int(string[-1])+1)
        new=int(string)+1
        return [int(val) for val in str(new)]
