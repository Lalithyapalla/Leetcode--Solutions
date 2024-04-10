class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        li,ri=0,len(nums)-1
        while li<=ri:
            mid=(li+ri)//2
            if nums[mid]<target:
                li=mid+1
            elif nums[mid]>target:
                ri=mid-1
            else:
                return (mid)
        return li
                

