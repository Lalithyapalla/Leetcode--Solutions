class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        new=[]
        for ele in nums:
            dig=str(ele)
            for char in dig:
                new+=[int(char)]
        return new
