class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        list=[]
        for i in range(rowIndex+1):
            new=[]
            for j in range(i+1):
                if j==0 or j==i:
                    new.append(1)
                else:
                    new.append(list[i-1][j-1]+list[i-1][j])
            list.append(new)
        return list[rowIndex]
