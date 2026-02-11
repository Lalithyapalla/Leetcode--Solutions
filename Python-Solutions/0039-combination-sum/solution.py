class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        temp=[]
        n=len(candidates)
        self.solve(0,temp,res,candidates,target,n)
        return res
    def solve(self,indx,temp,res,arr,t,n):
        if t==0:
            res.append(temp[:])
            return
        if t<0:
            return
        for i in range(indx,n):
            temp.append(arr[i])
            self.solve(i,temp,res,arr,t-arr[i],n)
            temp.pop()
